from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud
from app.database import get_db
from app.schemas import WalletRequestModel, WalletInfoResponse, \
    PaginatedHistoryResponse
from app.tron_client import get_wallet_info

router = APIRouter()


@router.post("/wallet", response_model=WalletInfoResponse)
def fetch_wallet_info(wallet_request: WalletRequestModel, db: Session = Depends(get_db)):
    data = get_wallet_info(wallet_request.address)
    # логируем запрос в БД
    crud.create_wallet_request(db, wallet_request.address)
    return data


@router.get("/history", response_model=PaginatedHistoryResponse)
def get_wallet_requests(page: int = 1, per_page: int = 10,
                        db: Session = Depends(get_db)):
    return crud.get_wallet_requests(db, page, per_page)
