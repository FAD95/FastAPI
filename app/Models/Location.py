# Python 
from typing import Optional

# Pydantic
from pydantic import BaseModel, Field


# Location
class Location(BaseModel):
    city: str = Field(
        ...,
        title="City",
        min_length=2,
        max_length=50
    )
    state: str = Field(
        ...,
        title="State",
        min_length=2,
        max_length=50
    )
    country: str = Field(
        ...,
        title="Country",
        min_length=2,
        max_length=50
    )
    address: Optional[str] = Field(
        title="Address",
        default=None,
        min_length=7,
        max_length=100
    )
    lat: Optional[float] = Field(
        title="Latitude",
        default=None
    )
    lon: Optional[float] = Field(
        title="Longitude",
        default=None
    )

    class Config:
        schema_extra = {
            "example": {
                "city": "Bogotá",
                "state": "Bogotá",
                "country": "Colombia",
                "address": "Rua dos Bobos, 123",
                "lat": -23.5,
                "lon": -46.6
            }
        }