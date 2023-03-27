from pydantic import BaseModel
from typing import List, Optional
from enum import Enum

class TranslateResult(BaseModel):
    original_content: str
    translated_content: str
    
class Document(BaseModel):
    id: Optional[str] = None
    text: str