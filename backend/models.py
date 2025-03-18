from sqlalchemy import Column, Integer, String, Float
from database import Base  # ✅ Make sure this import works

class Match(Base):
    __tablename__ = "matches"

    id = Column(Integer, primary_key=True, index=True)
    team1 = Column(String, nullable=False)
    team2 = Column(String, nullable=False)
    score = Column(String, nullable=True)
    goals_team1 = Column(Integer, nullable=False)
    goals_team2 = Column(Integer, nullable=False)
    possession_team1 = Column(Float, nullable=False)
    possession_team2 = Column(Float, nullable=False)
    fouls_team1 = Column(Integer, nullable=False)
    fouls_team2 = Column(Integer, nullable=False)

