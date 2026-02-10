"""Data Fetching API
Uses the GET method to obtain data from the sayings
file.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sayings import aphorisms

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/wisdom")
def wisdom():
    return aphorisms

# http://127.0.0.1:8000/wisdom