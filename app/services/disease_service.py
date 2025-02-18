from typing import List
from app.models.disease import Disease, DiseaseResponse
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class DiseaseService:
    def __init__(self):
        # TODO: Load disease database and ML models
        self.diseases = {
            "influenza": {
                "symptoms": ["fever", "cough", "fatigue", "body aches"],
                "description": "A viral infection that attacks your respiratory system",
                "treatments": ["antiviral medications", "rest", "fluids"]
            },
            "type_2_diabetes": {
                "symptoms": ["increased thirst", "frequent urination", "fatigue", "blurred vision"],
                "description": "A chronic condition that affects how your body metabolizes sugar",
                "treatments": ["metformin", "lifestyle changes", "insulin therapy"]
            }
        }
        self.vectorizer = TfidfVectorizer()

    def predict_disease(self, symptoms: List[str]) -> DiseaseResponse:
        """
        Predict disease based on symptoms using ML model
        """
        # Convert symptoms to string for vectorization
        input_symptoms = " ".join(symptoms)
        
        # Calculate similarity with known diseases
        max_similarity = 0
        predicted_disease = None
        
        for disease, info in self.diseases.items():
            disease_symptoms = " ".join(info["symptoms"])
            vectors = self.vectorizer.fit_transform([input_symptoms, disease_symptoms])
            similarity = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
            
            if similarity > max_similarity:
                max_similarity = similarity
                predicted_disease = disease
        
        if predicted_disease:
            disease_info = self.diseases[predicted_disease]
            return DiseaseResponse(
                disease=predicted_disease,
                confidence=float(max_similarity),
                possible_treatments=disease_info["treatments"],
                description=disease_info["description"]
            )
        
        return DiseaseResponse(
            disease="Unknown",
            confidence=0.0,
            possible_treatments=[],
            description="Unable to determine disease from given symptoms"
        )

    def get_disease_info(self, disease_name: str) -> Disease:
        """
        Get detailed information about a disease
        """
        if disease_name in self.diseases:
            info = self.diseases[disease_name]
            return Disease(
                name=disease_name,
                symptoms=info["symptoms"],
                description=info["description"]
            )
        return None 