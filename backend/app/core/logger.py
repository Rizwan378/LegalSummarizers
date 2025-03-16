import logging
import sys
from .config import settings

def setup_logging():
    logging.basicConfig(
        level=getattr(logging, settings.LOG_LEVEL),
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )

def configure_file_logging():
    """Add file handler for persistent logs."""
    from logging.handlers import RotatingFileHandler
    handler = RotatingFileHandler("logs/app.log", maxBytes=10*1024*1024, backupCount=5)
    handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
    logging.getLogger().addHandler(handler)
    logging.getLogger().info("Configured file logging with rotation")
