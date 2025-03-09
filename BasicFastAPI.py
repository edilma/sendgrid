import os
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
async def create_world(request: Request):
    body = await request.json()
    return body

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Get PORT from env, default to 8000
    uvicorn.run(app, host="0.0.0.0", port=port) # 0.0.0.0 listens on all interfaces.