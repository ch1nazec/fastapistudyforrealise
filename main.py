from fastapi import FastAPI, HTTPException
from typing import Optional
from pydantic import BaseModel


app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    age: int


class Post(BaseModel):
    id: int
    title: str
    body: str
    author: User


class PostCreate(BaseModel):
    title: str
    body: str
    author_id: int



users = [
    {
        'id': 1,
        'name': 'John',
        'age': 30
    },
    {
        'id': 2,
        'name': 'Danny',
        'age': 25
    },
    {
        'id': 3,
        'name': 'Pididid',
        'age': 18
    },
]
users = [User(**item) for item in users]

posts = [
    {
        'id': 1,
        'title': 'News 1',
        'body': 'Text 1',
        'author': users[0]
    },
    {
        'id': 2,
        'title': 'News 2',
        'body': 'Text 2',
        'author': users[1]
    },
    {
        'id': 3,
        'title': 'News 3',
        'body': 'Text 3',
        'author': users[2]
    },
]
posts = [Post(**item) for item in posts]


@app.get('/items')
async def items() -> list[Post]:
    return posts


@app.post('/items/add')
async def add_item(post: PostCreate) -> Post:
    author = next((user for user in users if user.id == post.author_id), None)
    if not author:
        raise HTTPException(status_code=404, detail='User doesnt exists.')
    new_post_id = len(posts) + 1

    new_post = {'id': new_post_id, 'title': post.title, 'body': post.body, 'author': author}
    posts.append(new_post)

    return new_post



@app.get('/items/{id}')
async def items(id: int) -> Post:
    for post in posts:
        if post.id == id:
            return post
    raise HTTPException(status_code=404, detail='Post not found')


@app.get('/search')
async def search(post_id: Optional[int] = None) -> dict[str, Optional[Post]]:
    if post_id:
        for post in posts:
            if post.id == post_id:
                return {'data': post}
        raise HTTPException(status_code=404, detail='Post not found')
    else:
        return {'data': None}