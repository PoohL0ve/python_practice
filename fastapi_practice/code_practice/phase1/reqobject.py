"""Using the Request Object in FastAPI
The data can only be viewed and should be used to understand
what may be occuring and the type of information that the 
system may receive.
"""
from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/inspect")
def inspect(request: Request):
    return {
        "method": request.method,
        "url": str(request.url),
        "headers": dict(request.headers),
        "client": request.client.host if request.client else None,
    }
