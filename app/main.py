from fastapi import FastAPI

from app.routers import wallet


app = FastAPI()
app.include_router(wallet.router)
