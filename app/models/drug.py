from pydantic import BaseModel
from typing import List, Optional, Dict

class DrugCandidate(BaseModel):
    smiles: str
    name: Optional[str] = None
    molecular_weight: float
    logp: float
    bioavailability: float
    toxicity: float
    source: str
    confidence: float
    research_references: Optional[List[str]] = None

class DrugProperty(BaseModel):
    name: str
    value: float
    unit: Optional[str] = None
    confidence: float

class DrugPrediction(BaseModel):
    smiles: str
    properties: Dict[str, DrugProperty]
    visualization_url: Optional[str] = None

class GeneratedMolecule(BaseModel):
    smiles: str
    parent_smiles: str
    similarity: float
    properties: Dict[str, DrugProperty]
    valid: bool 