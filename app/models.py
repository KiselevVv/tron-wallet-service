import uuid

from sqlalchemy import Column, DateTime, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()


class WalletRequest(Base):
    """Модель для хранения запросов на информацию о кошельке."""

    __tablename__ = "wallet_requests"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        index=True,
    )
    wallet_address = Column(String(42), nullable=False, index=True)
    timestamp = Column(DateTime, server_default=func.now(), index=True)
