from fastapi import Form,FastAPI
app=FastAPI()

@app.post("/login")
def login(username:str=Form(...),password:str=Form(...)):
    return {"username":username, "message": "logged in"}