"""Creating a Request Body
The BaseModel class from the Pydantic library is used to 
create request bodies. It allows you to define a data contract.

FastApi's job:
- Reads the request body as JSON
- Convert the data if needed
- Validate it: Will return an error if there is one
- Allow the function to receive the data as a Python object
- Generate JSON schema
"""
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Buddy(BaseModel):
    first_name: str
    last_name: str
    nickname: str | None = None # This is optional
    age: int
    heigth: float | None = None

@app.post("/buddy/")
def create_buddy(buddy: Buddy):
    return buddy

# All attributes of the model can be accessed in the function
# Such as buddy.first_name

@app.put("/buddy/{buddy_id}")
def update_buddy(buddy_id: int, buddy: Buddy):
    return {"buddy_id": buddy_id}