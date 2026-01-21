"""Response Object
FastAPI:
- enforces the response contract
- filters fields
- validates the output

It allows the developer to control what the client sees.
"""
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ItemIn(BaseModel):
    name: str
    price: float

class ItemOut(BaseModel):
    name: str

@app.post("/items/", response_model=ItemOut)
def create_item(item: ItemIn):
    return item
