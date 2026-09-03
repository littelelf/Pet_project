from datetime import datetime
from pydantic import BaseModel, Field, EmailStr, ConfigDict, field_validator, ValidationError
from fastapi import FastAPI
from typing import Annotated, Any, Self
import psycopg2,re


def password_check(v: str):
    # number, symbols, upper letter
    if len(v) < 8:
        raise ValueError("Password must have at least 8 characters")
    if not any ( char.isdigit() for char in v):
        raise ValueError("Password must have at least 1 digit")
    if not any ( char.isupper() for char in v):
        raise ValueError("Password must have at least 1 Upper letter")
    if not re.search(r"[@#$%*_]", v):
        raise ValueError("Password must have at least 1 symbol")
    return v


def name_check(value: str) -> str:
    # начинаться с заглавной буквы, все остальное с нижней
    def first_ch():
        pass
    def second_ch():
        pass
    def middle_ch():
        pass




#app = FastAPI()

class User(BaseModel):
    id: int

    first_name: str = Field(max_length=50)
    second_name: str = Field(max_length=50)
    middle_name: str = Field(max_length=50)
    #@field_validator("first_name", "second_name", "middle_name")
    #@classmethod


    age: int = Field(gt=0, lt=150) #todo conint чем отличается от этого

    email: EmailStr
    password: str
    @field_validator("password") #The @field_validator("password") method calls password_check(v) during validation.
    @classmethod
    def validate_password(cls, v: str) -> str:
        return password_check(v)

    sum: int = Field(gt=0, lt=150000)
    #deadline: datetime = field(gt=0, lt=datetime(year=2020, month=1, day=1)) #срок #todo faaah
    is_active: bool = False # типа базово она не принята

    income: float



# postgresql
#connection = psycopg2.connect()


# post - add
#@app.post("/users", response_model=User)
#async def create_user(user: User):




try:
    user = User(first_name="sdfsd", second_name="asdasd", middle_name="asda",
                age = 32, email = "asdas", password="raellos2", sum = 500,
                is_active=False, income = 10000)
except ValidationError as e:
    print(e.json(indent = 2))



