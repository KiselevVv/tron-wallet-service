from datetime import datetime
from typing import Optional, List
from uuid import UUID

from pydantic import BaseModel


class WalletRequestModel(BaseModel):
    """Модель данных для запроса информации о кошельке."""
    address: str

    class Config:
        from_attributes = True


class WalletInfoResponse(BaseModel):
    """Модель данных для ответа с информацией о кошельке."""
    address: str
    balance: Optional[int] = None
    bandwidth: Optional[int] = None
    energy: Optional[int] = None

    class Config:
        from_attributes = True


class WalletRequestHistoryResponse(BaseModel):
    """Модель для ответа с историей запросов на информацию о кошельке."""
    id: UUID
    wallet_address: str
    timestamp: datetime

    class Config:
        from_attributes = True


class PaginatedHistoryResponse(BaseModel):
    """Модель для ответа с пагинированной историей запросов."""
    page: int
    per_page: int
    total: int
    total_pages: int
    has_next: bool
    data: List[WalletRequestHistoryResponse]
