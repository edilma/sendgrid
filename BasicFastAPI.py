from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class Message(BaseModel):
    message: str

@app.get("/")
async def read_root():
    return {"message": "hello"}

@app.post("/world")
async def create_world(request:     Message):                                                                                       
    body = await request.json()
    return body

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)