# database_logic.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configura la URL de conexión a PostgreSQL para contenidos
DATABASE_URL = "postgresql://postgres:12345@localhost:5432/ASEE"

# Crea la base de datos para contenidos con SQLAlchemy
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

