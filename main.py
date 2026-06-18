from fastapi import FastAPI


app = FastAPI()


@app.get('/')
async def home() -> dict[str, str]:
    return {'data': 'mess'}


@app.get('/contacts')
async def contacts() -> int:
    return 1000


posts = 