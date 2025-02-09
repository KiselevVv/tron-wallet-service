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


@app.get("/history")
def get_wallet_requests(page: int = 1, per_page: int = 10, db: Session = Depends(get_db)):
    return crud.get_wallet_requests(db, page, per_page)

