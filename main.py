from fastapi import FastAPI
import json

app = FastAPI()

# Load JSON data
with open("anzsco_data.json", "r", encoding="utf-8") as f:
    anzsco_data = json.load(f)

@app.get("/")
def read_root():
    return {"message": "Welcome to the ANZSCO API!"}

@app.get("/anzsco")
def get_anzsco_data():
    return anzsco_data
