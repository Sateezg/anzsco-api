from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Enable CORS for all origins (Allow frontend to call API)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Load JSON Data
with open("anzsco_data.json", "r", encoding="utf-8") as f:
    anzsco_data = json.load(f)

@app.get("/")
def read_root():
    return {"message": "Welcome to the ANZSCO API! Use /anzsco/{code} to fetch details."}

# Fetch occupation details based on ANZSCO code
@app.get("/anzsco/{occupation_code}")
def get_occupation_data(occupation_code: str):
    result = [entry for entry in anzsco_data if entry.get("ANZSCO Code") == occupation_code]
    
    if result:
        return result
    return {"error": "Occupation code not found"}
