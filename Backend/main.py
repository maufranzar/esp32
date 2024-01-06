from fastapi import FastAPI
from pydantic import BaseModel




class SensorData(BaseModel):
    time: int
    temperature: int
    humidity: int
    
    
    
esp32 = FastAPI()


@esp32.post("/data/")
async def recieve_data(data:SensorData):
    print(data.dict())
    
    return {"message":"Data recieved"}
