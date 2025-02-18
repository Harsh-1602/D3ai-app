# D3AI - Disease-based Drug Discovery Platform

D3AI is an innovative drug discovery platform that leverages artificial intelligence to accelerate the drug candidate screening process for researchers and scientists.

## Features

- Disease prediction through symptom analysis
- Research paper analysis and drug candidate identification
- Integration with chemical databases (ChEMBL, ZINC)
- QSAR model for protein-drug activity prediction
- Molecular fingerprinting
- ADMET properties prediction
- Drug molecule generation using MegaMolBERT
- Structural validation of generated molecules
- Property-based filtering system

## Tech Stack

- Backend: FastAPI, Python
- Frontend: React, Three.js
- ML/AI: PyTorch, RDKit, Transformers
- Database: ChromaDB, MongoDB
- External APIs: ChEMBL, ZINC

## Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```
4. Run the backend:
   ```bash
   uvicorn app.main:app --reload
   ```
5. Run the frontend:
   ```bash
   cd frontend
   npm install
   npm run dev
   ```

## Project Structure

```
d3ai/
├── app/
│   ├── main.py
│   ├── models/
│   ├── services/
│   ├── utils/
│   └── api/
├── frontend/
│   ├── src/
│   └── public/
├── ml/
│   ├── qsar/
│   ├── fingerprint/
│   └── generation/
└── tests/
```

## License

MIT License 