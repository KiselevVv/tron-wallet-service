import uuid
from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from app.database import Base


class WalletRequest(Base):
    __tablename__ = "wallet_requests"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        index=True
    )
    wallet_address = Column(String(42), nullable=False)
    timestamp = Column(DateTime, server_default=func.now())
