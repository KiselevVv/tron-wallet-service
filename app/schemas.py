from pydantic import BaseModel


class WalletRequestModel(BaseModel):
    address: str
