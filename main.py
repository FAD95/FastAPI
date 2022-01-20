# Python 
from typing import Optional
from enum import Enum

# FastAPI
from fastapi import FastAPI, status
from fastapi import Body, Query, Path

# Models
from app.Models import Person, Location

app = FastAPI()

@app.get(
    path = "/",
    status_code = status.HTTP_200_OK
)
def home():
    return {"message": "Hello World"}

# Request and Response Body

@app.post(
    path = "/person/new",
    status_code = status.HTTP_201_CREATED,
    response_model = Person,
    response_model_exclude = {"password"}
)
def create_person(person: Person = Body(...)):
    return person.dict()


# Validations: Query Parameters

@app.get(
    path = "/person/detail",
    status_code = status.HTTP_200_OK
)
def show_person(
    name: Optional[str] = Query(
        None, 
        min_length=1, 
        max_length=50, 
        regex="^([A-Z])\w",
        tile="Person Name",
        description="This is the person name. It must be capitalised and between 1 and 50 characters.",
        example="Fadith"
        ), 
    age: int = Query(
        ...,
        title="Person Age", 
        description="This is the person age. It must be an integer and is required.",
        ge=15, 
        le=150,
        example=26
        ) #Also can use gt (>) and lt (<)
    ):
    return {name: age}

# Validations: Path Parameters

@app.get(
    path = "/person/detail/{person_id}",
    status_code = status.HTTP_200_OK
)
def show_person(
    person_id: int = Path(
        ..., 
        title="Person ID",
        description="This is the person ID. It must be an integer greater than 0 and is required.",
        gt=0,
        example=1
        )
    ):
    return {person_id: "It exists!"}

# Validations: Body Parameters

@app.put(
    path = "/person/update/{person_id}",
    status_code = status.HTTP_202_ACCEPTED
)
def update_person(
    person_id: int = Path(
        ..., 
        title="Person ID",
        description="This is the person ID. It must be an integer greater than 0 and is required.",
        gt=0,
        example=1
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
    return {person_id: result}