from fastapi import FastAPI
from googletrans import Translator

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}