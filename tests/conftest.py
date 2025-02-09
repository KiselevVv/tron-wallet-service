import pytest
from sqlalchemy import create_engine
from app.database import Base, SessionLocal
from app.core.config import settings


# Создание временной базы данных для тестирования
@pytest.fixture(scope="function")
def db():
    engine = create_engine(settings.DATABASE_URL)
    Base.metadata.create_all(bind=engine)

    SessionLocal.configure(bind=engine)
    db_session = SessionLocal()

    yield db_session

    db_session.close()
    Base.metadata.drop_all(bind=engine)
