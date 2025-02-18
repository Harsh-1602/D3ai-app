from fastapi import APIRouter, HTTPException
from typing import List
from app.models.disease import Disease, DiseaseResponse
from app.models.drug import DrugCandidate, DrugPrediction, GeneratedMolecule
from app.services.disease_service import DiseaseService
from app.services.drug_service import DrugService

router = APIRouter()
disease_service = DiseaseService()
drug_service = DrugService()

@router.post("/predict-disease", response_model=DiseaseResponse)
async def predict_disease(symptoms: List[str]):
    """
    Predict disease based on symptoms
    """
    try:
        prediction = disease_service.predict_disease(symptoms)
        return prediction
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/disease/{disease_name}", response_model=Disease)
async def get_disease_info(disease_name: str):
    """
    Get detailed information about a disease
    """
    disease_info = disease_service.get_disease_info(disease_name)
    if disease_info is None:
        raise HTTPException(status_code=404, detail="Disease not found")
    return disease_info

@router.get("/drug-candidates/{disease}", response_model=List[DrugCandidate])
async def search_drug_candidates(disease: str):
    """
    Search for drug candidates based on disease
    """
    try:
        candidates = drug_service.search_candidates(disease)
        return candidates
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/generate-molecules", response_model=List[GeneratedMolecule])
async def generate_molecules(smiles: str, n_molecules: int = 5):
    """
    Generate new molecules based on seed molecule
    """
    try:
        if not drug_service.validate_structure(smiles):
            raise HTTPException(status_code=400, detail="Invalid SMILES string")
        
        molecules = drug_service.generate_molecules(smiles, n_molecules)
        return molecules
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/predict-properties", response_model=DrugPrediction)
async def predict_properties(smiles: str):
    """
    Predict properties of a molecule
    """
    try:
        if not drug_service.validate_structure(smiles):
            raise HTTPException(status_code=400, detail="Invalid SMILES string")
        
        prediction = drug_service.predict_properties(smiles)
        if prediction is None:
            raise HTTPException(status_code=400, detail="Failed to predict properties")
        return prediction
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/validate-structure")
async def validate_structure(smiles: str):
    """
    Validate if a SMILES string represents a valid molecule
    """
    try:
        is_valid = drug_service.validate_structure(smiles)
        return {"valid": is_valid}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 