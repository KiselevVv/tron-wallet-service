from fastapi import FastAPI

from app.database import Base, engine
from app.routers import wallet

# создаем таблицу в БД, если отсутсвует
Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(wallet.router)
