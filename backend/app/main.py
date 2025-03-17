from fastapi import FastAPI
from .api.endpoints import summarizer
from .core.config import settings
from .core.logger import setup_logging
import logging

setup_logging()
logger = logging.getLogger(__name__)

app = FastAPI(title="LegalSummarizer Assessment API")

app.include_router(summarizer.router, prefix="/api/v1")

@app.get("/health")
async def health_check():
    """Check API health and OpenAI connectivity."""
    try:
        client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)
        await client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "ping"}])
        return {"status": "healthy"}
    except Exception as e:
        logger.error(f"Health check failed: {str(e)}")
        return {"status": "unhealthy", "error": str(e)}

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health_check():
    """Check API health and OpenAI connectivity."""
    try:
        client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)
        await client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "ping"}])
        return {"status": "healthy"}
    except Exception as e:
        logger.error(f"Health check failed: {str(e)}")
        return {"status": "unhealthy", "error": str(e)}

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
