# Python 
from typing import Optional

# Pydantic
from pydantic import BaseModel

# FastAPI
from fastapi import FastAPI, Body, Query

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
    name: Optional[str] = Query(None, min_length=1, max_length=50, regex="^[A-Z]+[a-zA-Z]+$"), 
    age: int = Query(..., ge=15, le=150) #Also can use gt (>) and lt (<)
    ):
    return {name: age}