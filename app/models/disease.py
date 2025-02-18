from pydantic import BaseModel
from typing import List, Optional

class Disease(BaseModel):
    name: str
    symptoms: List[str]
    description: Optional[str] = None
    category: Optional[str] = None

class DiseaseResponse(BaseModel):
    disease: str
    confidence: float
    possible_treatments: List[str]
    description: str 