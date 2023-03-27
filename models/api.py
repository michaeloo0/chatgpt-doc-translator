from models.models import (
  TranslateResult
)
from pydantic import BaseModel
from typing import List, Optional

class TranslateResponse(BaseModel):
    results: List[TranslateResult]