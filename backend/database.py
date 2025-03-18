from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Use the Render database URL from environment variables
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://sports_db_6xgp_user:CEEnimCIVPiGtTxLVzIVjU9HkcbuvtxK@dpg-cvcs9d0fnakc739ajii0-a/sports_db_6xgp")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
