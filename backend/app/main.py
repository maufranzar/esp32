from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel

class SensorData(BaseModel):
    time: int
    temperature: int
    humidity: int
    light: float

app = FastAPI()

@app.on_event("startup")
async def startup_db_client():
    app.mongodb_client = AsyncIOMotorClient('mongodb://localhost:27017')
    app.mongodb = app.mongodb_client['esp32']

 
@app.on_event("shutdown")
async def shutdown_db_client():
    app.mongodb_client.close()

@app.post("/data/")
async def recieve_data(data: SensorData):
    collection = app.mongodb['sensor']
    sensor_data = data.dict()
    await collection.insert_one(sensor_data)
    return {"message": "Data received"}