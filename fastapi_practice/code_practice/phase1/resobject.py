"""Using the Response Object in FastAPI
This data can be altered.
"""
from fastapi import FastAPI, Response

app = FastAPI()

@app.get("/custom")
def custom(response: Response):
    response.status_code = 202
    response.headers["X-Notice"] = "Accepted but not processed"
    return {"message": "Check later"}
