from fastapi import FastAPI,Depends

app=FastAPI()

class commonqueryparams:
    def __init__(self,q:str|None=None,page:int=1,page_size:int=20):
        self.q=q
        self.page=page
        self.page_size=page_size


@app.get("/search")
def search(common:commonqueryparams=Depends(commonqueryparams)):
    return {
        "q":common.q,
        "page":common.page,
        "page_size":common.page_size
    }

@app.get("/search/short")
def search_short(common:commonqueryparams=Depends()):
    return {
        "q":common.q,
        "page":common.page,
        "page_size":common.page_size
    }