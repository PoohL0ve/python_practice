"""Contracts and Validation
This simple project displays:
- Data modelling
- Schema Enforcement
- Enum constraints
- Field Validations
- Automatic documentation
"""
from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel, Field, field_validator

app = FastAPI()

# Enum: First strict contract
class PriorityLevel(str, Enum):
    """
    Rejects any priority level that isn't "low", "medium", or
    "high" without using conditionals.
    """
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

# Request Model: Explicit Contract
class SignalRequest(BaseModel):
    """
    Provides an explicit contract and determines validation
    and ownership of incoming data. The class takes ownership
    of the input logic by specifying how it should be
    transformed. This eliminates the need for the route function
    to define the logic for the data.
    """
    message: str = Field(..., min_length=5, max_length=200)
    priority: PriorityLevel
    sender: str = Field(..., min_length=2, max_length=50)

    # Place Logic in here for input data
    @field_validator("message")
    @classmethod
    def normalize_message(cls, value: str) -> str:
        """Converts the string to lowercase"""
        return value.strip().lower()

    @field_validator("sender")
    @classmethod
    def normalize_sender(cls, value: str) -> str:
        """Removes whitespace from the string"""
        return value.strip()

# Response Model: Promised response
class SignalResponse(BaseModel):
    """
    SignalResponse provides a promise for the structure of the
    output data.
    """
    received: bool
    normalized_message: str
    priority_score: int

    @property
    def priority_score(self) -> int:
        """
        Converts the priority string level to the appropriate
        interger such as 1, 2, or 3.
        """
        score_map = {
            PriorityLevel.LOW: 1,
            PriorityLevel.MEDIUM: 2,
            PriorityLevel.HIGH: 3
        }
        return score_map[self.priority]

# End Point
@app.post("/signal", response_model=SignalResponse)
def receive_signal(payload: SignalRequest):
    """
    The route that uses the defined response model to send output
    to the user.
    """

    return SignalResponse(
        received=True,
        normalized_message=payload.message,
        priority_score=payload.priority
    )
