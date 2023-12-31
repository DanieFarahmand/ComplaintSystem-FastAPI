from fastapi import FastAPI

from database import database
from resources.routers import api_router

app = FastAPI(debug=True)
app.include_router(api_router)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
