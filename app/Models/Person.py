# Python 
from typing import Optional

# Pydantic
from pydantic import BaseModel, Field

# Models
from .HairColor import HairColor


# Person
class Person(BaseModel):
    first_name: str = Field(
        ..., 
        title="First Name", 
        min_length=2, 
        max_length=50
        )
    last_name: str = Field(
        ..., 
        title="Last Name", 
        min_length=2, 
        max_length=50
        )
    age: int = Field(
        ..., 
        title="Age", 
        gt=0, 
        lt=150
        )
    phone: Optional[str] = Field(
        title="Phone Number",
        default=None
        )
    hair_color: Optional[HairColor] = Field(
        title="Hair Color",
        default=None
        )
    is_married: Optional[bool] = Field(
        title="Is Married",
        default=False
    )
    password: str = Field(
        ..., 
        title="Password",
        min_length=8, 
        max_length=100
    )

    class Config:
        schema_extra = {
            "example": {
                "first_name": "Fadith",
                "last_name": "Escorcia",
                "age": 26,
                "phone": "555-555-5555",
                "hair_color": "brown",
                "is_married": False,
                "password": "password"
            }
        }