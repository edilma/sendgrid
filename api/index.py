from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/register")
async def register():
    return JSONResponse(content={"message": "ok"})

# Vercel requires a handler function
handler = app 