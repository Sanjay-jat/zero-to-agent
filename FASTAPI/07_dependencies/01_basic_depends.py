from fastapi import FastAPI,Depends

app=FastAPI()

def common_params(skip:int=0,limit:int=10):
    return {"skip":skip,"limit":limit}


@app.get("/items")
def get_items(params:dict=Depends(common_params)):
    return {"params":params}


@app.get("/users")
def get_users(params:dict=Depends(common_params)):
    return {"params":params}
