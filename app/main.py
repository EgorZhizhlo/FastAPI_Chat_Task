from fastapi import FastAPI


app = FastAPI()
ROOT_URL = '/api'


@app.get(ROOT_URL + '')
async def root():
    return {"message": "Hello, World!"}
