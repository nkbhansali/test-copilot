from fastapi import FastAPI
from .routers import flights

app = FastAPI()

app.include_router(flights.router)
