from fastapi import FastAPI, HTTPException, status
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import Body


app = FastAPI()
class UserBase(BaseModel):
    username:str
    email:str

class UserIn(UserBase):
    username:str
    email:str
    password: str

class UserOut(UserBase):
    username: str
    email: str

class UserInDB(UserBase):
    username:str
    email:str
    password: str
    hashed_password: str


@app.post("/users",response_model =UserOut)
def create_users(userin:UserIn):
    hashed_password = "hashed_" + userin.password
    user_in_db=UserInDB(**userin.dict(),hashed_password=hashed_password)
    return user_in_db

