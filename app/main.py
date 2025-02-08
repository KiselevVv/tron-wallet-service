from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app import crud
from app.database import SessionLocal, Base, engine
from app.tron_client import get_wallet_info


Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/wallet")
def fetch_wallet_info(address: str, db: Session = Depends(get_db)):
    data = get_wallet_info(address)

    # логируем запрос в БД
    crud.create_wallet_request(db, address)

    return data


