import pandas as pd
import pickle
from sqlalchemy.orm import Session
from database import SessionLocal, Match
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler

# Step 1: Load data from PostgreSQL
def load_data():
    db: Session = SessionLocal()
    matches = db.query(Match).all()
    db.close()

    # Convert match data to Pandas DataFrame
    data = [
        [m.goals_team1, m.goals_team2, m.possession_team1, m.possession_team2, m.fouls_team1, m.fouls_team2, 
         1 if m.goals_team1 > m.goals_team2 else 0 if m.goals_team1 < m.goals_team2 else 2]
        for m in matches
    ]
    
    df = pd.DataFrame(data, columns=["goals_team1", "goals_team2", "possession_team1", "possession_team2", "fouls_team1", "fouls_team2", "result"])
    return df

# Step 2: Train the AI model
def train_model():
    df = load_data()

    if df.empty:
        print("No match data available for training.")
        return

    X = df.drop(columns=["result"])
    y = df["result"]

    # Standardize features
    scaler = StandardScaler()
    X = scaler.fit_transform(X)

    # Split data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a Random Forest model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Save the trained model and scaler
    with open("models/match_predictor.pkl", "wb") as f:
        pickle.dump(model, f)
    with open("models/scaler.pkl", "wb") as f:
        pickle.dump(scaler, f)

    print("✅ AI Model Trained & Saved!")

if __name__ == "__main__":
    train_model()
