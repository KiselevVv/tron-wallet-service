from fastapi import FastAPI, HTTPException

from app.tron_client import get_wallet_info

app = FastAPI()


@app.post("/wallet")
def fetch_wallet_info(address: str):
    data = get_wallet_info(address)
    return data


