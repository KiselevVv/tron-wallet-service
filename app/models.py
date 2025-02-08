from sqlalchemy import Column, Integer, String, DateTime
from app.database import Base
from sqlalchemy.sql import func


class WalletRequest(Base):
    __tablename__ = "wallet_requests"

    id = Column(Integer, primary_key=True, index=True)
    wallet_address = Column(String, nullable=False)
    timestamp = Column(DateTime, default=func.now())
