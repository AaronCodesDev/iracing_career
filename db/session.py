from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pathlib import Path

# Base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# Archivo SQLite dentro de data/
DB_PATH = BASE_DIR / "data" / "iracing_career.db"

engine = create_engine(f"sqlite:///{DB_PATH}", echo=True)
SessionLocal = sessionmaker(bind=engine)
