import pandas as pd
from typing import List
from ..models.question import Question

def validate_csv_content(content: bytes) -> List[str]:
    """Validate CSV content and extract questions."""
    try:
        df = pd.read_csv(pd.io.common.StringIO(content.decode('utf-8')))
        if 'QuestionText' not in df.columns:
            raise ValueError("CSV must contain 'QuestionText' column")
        return df['QuestionText'].dropna().tolist()
    except Exception as e:
        raise ValueError(f"Invalid CSV content: {str(e)}")

def check_csv_size(content: bytes) -> None:
    """Validate CSV file size against max limit."""
    max_size = settings.MAX_CSV_SIZE
    if len(content) > max_size:
        raise ValueError(f"CSV file size exceeds limit of {max_size / (1024*1024)} MB")
    logger.info(f"CSV size validated: {len(content)} bytes")
    if len(content) == 0:
        raise ValueError("CSV file is empty")
    return None

def check_csv_size(content: bytes) -> None:
    """Validate CSV file size against max limit."""
    max_size = settings.MAX_CSV_SIZE
    if len(content) > max_size:
        raise ValueError(f"CSV file size exceeds limit of {max_size / (1024*1024)} MB")
    logger.info(f"CSV size validated: {len(content)} bytes")
    if len(content) == 0:
        raise ValueError("CSV file is empty")
    return None
