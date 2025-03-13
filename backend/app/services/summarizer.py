import re
import json
import asyncio
import logging
from openai import AsyncOpenAI
from ..core.config import settings

logger = logging.getLogger(__name__)

client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)

def get_prompt():
    return '''You are a legal assistant tasked with summarizing legal questions into a one-line ideal summary. The summary must capture the main legal issue, key parties involved, and brief context if necessary. If a state is explicitly mentioned in the question, include its state code in parentheses at the end (e.g., (NV)). If no state is mentioned, do not include a state code. Ensure the summary is concise and fits on one line.

    Guidelines:
    - Identify the main legal issue (e.g., eviction, custody, contract dispute).
    - Mention the key parties involved (e.g., sister, landlord, tenant).
    - Include brief context if it clarifies the issue.
    - Include the state code only if explicitly stated in the question—do not infer or guess.
    - If the question is short, the summary may resemble it but should still focus on the legal essence.
    - For unclear questions, summarize based on available information.
    - If multiple states are mentioned, include the state most relevant to the legal issue.
    - If the input is not a legal question or is nonsensical, respond with 'Not a valid legal question'.

    Examples:
    - Input: "My sister and 17 yr old nephew is living in my fathers house, moved back in a few months ago. If my father passes the house is in a trust to be sold and divided between 5 siblings. Nevada, can she refuse to move and would I have to evict her? I am the co-trustee and the executor of the estate (house, no real noon real money?"
      Output: "Eviction of sister and nephew living in father's house (NV)"

    - Input: "I live in Texas but work in Oklahoma. Can I sue my employer for wrongful termination?"
      Output: "Suing employer for wrongful termination (OK)"

    - Input: "Is it legal to record phone calls?"
      Output: "Legality of recording phone calls"

    - Input: "hello I recently got denied my Motion for a stay of writ of possession. However the landlord stated at court that they would still take my past due payments. However i need to know if i make my payment directly to the landlord even though a writ of possession has already been signed as of Oct.21,2022. Can they stop the writ by notifying the sheriff';s office and courts? I filed an emergency stay of writ of possession and was denied on Nov.19 Maine no that is all"
      Output: "Stopping writ of possession via payment and landlord notification (ME)"

    - Input: "My neighbor is loud. What can I do?"
      Output: "Possible noise complaint or nuisance issue"

    - Input: "asdf qwerty"
      Output: "Not a valid legal question."

    - Input: "What is the capital of France?"
      Output: "Not a valid legal question"

    Input:
      Now, summarize the following legal questions:
      {}

    Output:
      Provide a response **ONLY** in this format:
      ```json
      [
      {
      "QuestionText": "<Text of Questiontext>",
      "Summary": "<Summary of Questiontext>"
      },
      {
      "QuestionText": "<Text of Questiontext>",
      "Summary": "<Summary of Questiontext>"
      }
      ]
      ```'''

def clean_json_response(response_text):
    if response_text.startswith("```json") and response_text.endswith("```"):
        response_text = response_text.split("\n", 1)[1].rsplit("\n", 1)[0].strip()
    return response_text

def preprocess_question(question):
    question = re.sub(r'https?://\S+|www\.\S+', '', question)
    question = re.sub(r'[^A-Za-z0-9.,?\'\"() ]+', '', question)
    question = re.sub(r'\s+', ' ', question).strip()
    return question

async def generate_summaries(questions):
    batch_size = 10
    summaries = []
    tasks = []

    async def fetch_summary(batch):
        formatted_input = "\n".join(batch)
        prompt = get_prompt().format(formatted_input)
        try:
            response = await client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                temperature=0,
                seed=1
            )
            raw_content = response.choices[0].message.content
            cleaned_response = clean_json_response(raw_content)
            return json.loads(cleaned_response)
        except Exception as e:
            logger.error(f"Error fetching summaries: {str(e)}")
            return [{"QuestionText": q, "Summary": "Error processing question"} for q in batch]

    for i in range(0, len(questions), batch_size):
        batch = [preprocess_question(q) for q in questions[i:i+batch_size]]
        tasks.append(fetch_summary(batch))

    results = await asyncio.gather(*tasks)
    for batch_summaries in results:
        summaries.extend(batch_summaries)

    return summaries

def validate_summary(summary: dict) -> bool:
    """Validate summary format and content."""
    if not isinstance(summary, dict):
        logger.error("Summary must be a dictionary")
        return False
    if "QuestionText" not in summary or "Summary" not in summary:
        logger.error("Missing required summary fields")
        return False
    if not isinstance(summary["Summary"], str):
        logger.error("Summary field must be a string")
        return False
    logger.info("Summary validated successfully")
    return True
