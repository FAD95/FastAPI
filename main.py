# Python 
from typing import Optional

# Pydantic
from pydantic import BaseModel

# FastAPI
from fastapi import FastAPI
from fastapi import Body, Query, Path

app = FastAPI()
class Person(BaseModel):
    first_name: str
    last_name: str
    age: int
    address: Optional[str] = None
    phone: Optional[str] = None
    hair_color: Optional[str] = None
    is_married: Optional[bool] = None


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