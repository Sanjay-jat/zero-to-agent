from fastapi import FastAPI
from pydantic import BaseModel,Field
app=FastAPI()

class Address(BaseModel):
    city:str=Field(...,min_length=2,max_length=50)
    pincode: str = Field(..., min_length=6, max_length=6)

class Customer(BaseModel):
    name:str=Field(...,min_length=2,max_length=50)
    age: int = Field(..., gt=0, le=120)
    address:Address

@app.post("/customers")
def make_customer(customers:Customer):
    return customers.dict()