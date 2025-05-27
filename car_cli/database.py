# car_cli/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Use SQLite
engine = create_engine("sqlite:///./cars.db", connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

db_session = SessionLocal()


def init_db():
    """Create database tables if they don't exist."""
    from car_cli.models import Car  # avoid circular imports
    Base.metadata.create_all(bind=engine)