import os
from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr
from typing import Optional
import uvicorn

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with your WordPress domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    message: str

class RegistrationData(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    city: str
    country: str
    phone: Optional[str] = None

@app.get("/")
async def read_root():
    return {"message": "hello"}

@app.post("/world")
async def create_world(request: Request):
    body = await request.json()
    return body

@app.post("/register")
async def register(data: RegistrationData):
    try:
        # Here you would typically save the data to a database
        # For now, we'll just return the received data
        return {
            "status": "success",
            "message": "Registration successful",
            "data": {
                "email": data.email,
                "first_name": data.first_name,
                "last_name": data.last_name,
                "city": data.city,
                "country": data.country,
                "phone": data.phone
            }
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Get PORT from env, default to 8000
    uvicorn.run(app, host="0.0.0.0", port=port) # 0.0.0.0 listens on all interfaces.

    #Being deployed on vercel
    #sendgrid-sable-omega.vercel.app
