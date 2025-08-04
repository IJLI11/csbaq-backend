from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow all origins for demo purposes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CSBAQRequest(BaseModel):
    responses: Dict[int, int]  # Expecting keys Q1 to Q43, as integers

@app.post("/score")
def score_csbaq_plus(data: CSBAQRequest):
    responses = data.responses
    if len(responses) != 43:
        raise HTTPException(status_code=400, detail="All 43 questions must be answered.")

    traits = {
        "Openness":      [15, 16, 19, 22, 23, 39],
        "Conscientiousness": [1, 4, 8, 10, 12,]()
