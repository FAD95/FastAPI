from email import message
from pydantic import BaseModel, Field

class LoginOut(BaseModel):
    username: str = Field(
        ...,
        title="Email",
        description="This is the email. It must be a string and is required.",
        example="fad",
        min_length=3,
        max_length=20
    )
    message: str = Field(
        title="Message",
        default="Login successful!",
    )