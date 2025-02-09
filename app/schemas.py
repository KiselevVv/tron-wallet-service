from datetime import datetime
from typing import Optional, List
from uuid import UUID

from pydantic import BaseModel


class WalletRequestModel(BaseModel):
    address: str

    class Config:
        from_attributes = True


class WalletInfoResponse(BaseModel):
    address: str
    balance: Optional[int] = None
    bandwidth: Optional[int] = None
    energy: Optional[int] = None

    class Config:
        from_attributes = True


class WalletRequestHistoryResponse(BaseModel):
    id: UUID
    wallet_address: str
    timestamp: datetime

    class Config:
        from_attributes = True


class PaginatedHistoryResponse(BaseModel):
    page: int
    per_page: int
    total: int
    total_pages: int
    has_next: bool
    data: List[WalletRequestHistoryResponse]
