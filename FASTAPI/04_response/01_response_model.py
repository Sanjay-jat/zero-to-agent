from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import Body

app=FastAPI()

class UserIn(BaseModel):
    username:str
    email:str
    password: str

class UserOut(BaseModel):
    username: str
    email: str


@app.post("/register",response_model=UserOut)
def register(userin:UserIn):
    return {**userin.dict()}