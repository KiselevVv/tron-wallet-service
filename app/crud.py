from sqlalchemy.orm import Session
from app.models import WalletRequest


def create_wallet_request(db: Session, wallet_address: str):
    db_wallet_request = WalletRequest(wallet_address=wallet_address)

    db.add(db_wallet_request)
    db.commit()
    db.refresh(db_wallet_request)
    return db_wallet_request
