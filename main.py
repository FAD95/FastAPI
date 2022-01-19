# Python 
from typing import Optional
from enum import Enum

# Pydantic
from pydantic import BaseModel, Field

# FastAPI
from fastapi import FastAPI
from fastapi import Body, Query, Path

app = FastAPI()

# Models

## Hair Color 

class HairColor(Enum):
    BLOND = "blond"
    BROWN = "brown"
    BLACK = "black"
    RED = "red"
    WHITE = "white"
    GRAY = "gray"
    DYED = "dyed"
    COLOR_UNKNOWN = "color_unknown"

## Person
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


## Location
class Location(BaseModel):
    city: str
    state: str
    country: str
    address: Optional[str] = None
    lat: Optional[float] = None
    lon: Optional[float] = None



@app.get("/")
def home():
    return {"message": "Hello World"}

# Request and Response Body

@app.post("/person/new")
def create_person(person: Person = Body(...)):
    return person.dict()


# Validations: Query Parameters

@app.get("/person/detail")
def show_person(
    name: Optional[str] = Query(
        None, 
        min_length=1, 
        max_length=50, 
        regex="^([A-Z])\w",
        tile="Person Name",
        description="This is the person name. It must be capitalised and between 1 and 50 characters."
        ), 
    age: int = Query(
        ...,
        title="Person Age", 
        description="This is the person age. It must be an integer and is required.",
        ge=15, 
        le=150
        ) #Also can use gt (>) and lt (<)
    ):
    return {name: age}

# Validations: Path Parameters

@app.get("/person/detail/{person_id}")
def show_person(
    person_id: int = Path(
        ..., 
        title="Person ID",
        description="This is the person ID. It must be an integer greater than 0 and is required.",
        gt=0
        )
    ):
    return {person_id: "It exists!"}

# Validations: Body Parameters

@app.put("/person/update/{person_id}")
def update_person(
    person_id: int = Path(
        ..., 
        title="Person ID",
        description="This is the person ID. It must be an integer greater than 0 and is required.",
        gt=0
        ), 
    person: Person = Body(
        ...,
        title="Person",
        description="This is the person. It must be an object and is required.",
        ),
    location: Location = Body(
        ...,
        title="Location",
        description="This is the location. It must be an object and is required.",
        )
    ):
    # To create only one object, use the following syntax:
    result = person.dict()
    result.update(location.dict())
    return result