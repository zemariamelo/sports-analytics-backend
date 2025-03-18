from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://sports_user:password123@localhost/sports_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

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

Base.metadata.create_all(bind=engine)
