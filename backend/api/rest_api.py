from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from amadeus_handler import AmadeusHandler

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,)

@app.get("/api/get-popular-travel")
def get_popular_travel(origins:str = "MAD"):
    with AmadeusHandler() as api:
        return api.get_popular_destinations(origins)