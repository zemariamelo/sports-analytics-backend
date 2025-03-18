import pickle
import numpy as np
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import Base, SessionLocal
from models import Match  # ✅ Import Match from models.py

app = FastAPI()

# Load trained AI model
with open("models/match_predictor.pkl", "rb") as f:
    model = pickle.load(f)
with open("models/scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

# Database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ✅ **Test Route: API Health Check**
@app.get("/")
def home():
    return {"message": "Welcome to the Sports Analytics API"}

# ✅ **New Route: Get All Matches from DB**
@app.get("/matches")
def get_matches(db: Session = Depends(get_db)):
    matches = db.query(Match).all()
    return matches

# Define input schema for AI predictions
class MatchPredictionRequest(BaseModel):
    goals_team1: int
    goals_team2: int
    possession_team1: float
    possession_team2: float
    fouls_team1: int
    fouls_team2: int

# ✅ **Route: Predict match outcome using AI**
@app.post("/predict")
def predict_match(request: MatchPredictionRequest):
    input_data = np.array([
        [request.goals_team1, request.goals_team2, request.possession_team1, request.possession_team2, request.fouls_team1, request.fouls_team2]
    ])

    # Scale input data
    input_data = scaler.transform(input_data)

    # Predict outcome
    prediction = model.predict(input_data)[0]
    
    result_map = {1: "Team 1 Wins", 0: "Team 2 Wins", 2: "Draw"}
    
    return {"prediction": result_map[prediction]}
