'''Explanation of a simple request/response lifecycle

Steps that indicates the function runs near the middle:
- Client sends a GET/ping requests
- Server receives raw HTTP data and passes the request to the FastAPI app
- App checks the routing table to match ping + GET request
- No validation or dependency check is needed as the function has no parameters
- A ping() function executes and a dictionary is returned
- FastAPI serialises the dictionary to JSON and the HTTP response is sent

'''

from fastapi import FastAPI

app = FastAPI() # container for the system

# Ping Function: Sends a requests and receives a response
@app.get("/ping")
def ping():
    # returns a dictionary
    return {"message": "pong"}