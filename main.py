from fastapi import FastAPI


app = FastAPI()


@app.get('/')
def home():
    return [1,5,10]

