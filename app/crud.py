from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from app.models import WalletRequest


def create_wallet_request(db: Session, wallet_address: str):
    """Создаёт запись о запросе на информацию о кошельке."""
    try:
        db_wallet_request = WalletRequest(wallet_address=wallet_address)
        db.add(db_wallet_request)
        db.commit()
        db.refresh(db_wallet_request)
        return db_wallet_request
    except SQLAlchemyError as e:
        db.rollback()
        raise RuntimeError(f"Ошибка базы данных: {e}")


def get_wallet_requests(db: Session, page: int = 1, per_page: int = 10):
    """Получает историю запросов на информацию о кошельках с пагинацией."""
    try:
        query = db.query(WalletRequest)
        total_records = query.count()
        total_pages = (total_records + per_page - 1) // per_page
        offset = (page - 1) * per_page

        records = (
            db.query(WalletRequest)
            .order_by(WalletRequest.timestamp.desc())
            .offset(offset)
            .limit(per_page)
            .all()
        )

        return {
            "page": page,
            "per_page": per_page,
            "total": total_records,
            "total_pages": total_pages,
            "has_next": page < total_pages,
            "data": records,
        }
    except SQLAlchemyError as e:
        raise RuntimeError(f"Ошибка базы данных: {e}")
