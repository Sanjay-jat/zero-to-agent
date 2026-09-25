from fastapi import FastAPI

app=FastAPI()

@app.get("/")
async def greet():
    return {"message":"Hello Sanju"}

@app.get("/health")
def get_health():
    return {"status":"Ok"}

