from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.models import Base

DATABASE_URL = "sqlite:///ecotrack.db"

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(bind=engine)

Base.metadata.create_all(bind=engine)