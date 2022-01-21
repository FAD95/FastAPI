# Python 
from typing import Optional

# Pydantic
from pydantic import EmailStr 

# FastAPI
from fastapi import FastAPI, status
from fastapi import Body, Query, Path, Form, Header, Cookie

# Models
from app.Models import Person, Location, LoginOut

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

# Form Parameters

@app.post(
    path = "/login",
    status_code = status.HTTP_200_OK,
    response_model = LoginOut,
)
def login(
    username: str = Form(...),
    password: str = Form(...)
    ):
    return LoginOut(username=username)

@app.post(
    path = "/contact",
    status_code = status.HTTP_200_OK
)
def contact(
    first_name: str = Form(
        ...,
        title="First Name",
        description="This is the first name. It must be a string and is required.",
        min_length=3,
        max_length=50
    ),
    last_name: str = Form(
        ...,
        title="Last Name",
        description="This is the last name. It must be a string and is required.",
        min_length=3,
        max_length=50
    ),
    email: EmailStr = Form(...,
        title="Email",
        description="This is the email. It must be a string and is required.",
    ),
    message: str = Form(...,
        title="Message",
        description="This is the message. It must be a string and is required.",
        min_length=20,
        max_length=500
    ),
    user_agent: Optional[str] = Header(default=None),
    ads: Optional[str] = Cookie(default=None)
    ):
    return {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "message": message,
        "user_agent": user_agent,
        "ads": ads
    }
