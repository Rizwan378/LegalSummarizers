# LegalSummarizer

LegalSummarizer is a production-ready application for summarizing legal questions using OpenAI's GPT-3.5-turbo model.

## Features
- Upload CSV files with legal questions
- Generate concise summaries with state codes
- Responsive React frontend
- Scalable FastAPI backend
- Dockerized services with CI/CD

## Installation
1. Clone the repo: `git clone https://github.com/your-username/LegalSummarizer.git`
2. Configure `.env`: Update `backend/.env` with OpenAI API key
3. Build and run: `docker-compose up --build`
4. Access frontend: http://localhost:3000
5. Access API: http://localhost:8000/docs
6. Verify Redis: Ensure port 6379 is accessible
