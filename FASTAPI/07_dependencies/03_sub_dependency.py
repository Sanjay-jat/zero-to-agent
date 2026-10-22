from fastapi import Depends, FastAPI,HTTPException

app=FastAPI()

def get_raw_token(token:str|None=None):
    return token
def current_user(token:str=Depends(get_raw_token)):
    if not token:
        raise HTTPException(status_code=401,detail="user not authenticated")
    else:
        return {"username":f"user_{token}"}

@app.get("/profile")
def profile(user:dict=Depends(current_user)):
    return user