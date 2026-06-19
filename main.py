from fastapi import FastAPI, HTTPException, Path, Query, Body, Depends
from typing import Optional, Annotated
from sqlalchemy.orm import Session
from schemas import User as DBUser, PostCreate, UserCreate, PostResponse

from models import Post, User, Base
from database import engine, session_local


app = FastAPI()
Base.metadata.create_all(engine)

def get_db():
    db = session_local()
    try:
        yield db
    except BaseException as err:
        db.rollback()
        
        print(err)
        db.close()
    finally:
        db.close()


@app.post('/users/', response_model=DBUser)
async def create_user(user: UserCreate, db: Session = Depends(get_db)) -> User:
    db_user = User(name=user.name, age=user.age)
    db.add(db_user)

    db.commit()
    db.refresh(db_user)

    return db_user






# def check_user(user: str, users: list[dict]):
#     users_name = set(user.get('user') for user in users)
#     return True if not(user in users_name) else False


# @app.get('/items')
# async def items() -> list[Post]:
#     return posts


# @app.post('/items/add')
# async def add_item(post: PostCreate) -> Post:
#     author = next((user for user in users if user.id == post.author_id), None)
#     if not author:
#         raise HTTPException(status_code=404, detail='User doesnt exists.')
#     new_post_id = len(posts) + 1

#     new_post = {'id': new_post_id, 'title': post.title, 'body': post.body, 'author': author}
#     posts.append(new_post)

#     return new_post



# @app.get('/items/{id}')
# async def items(id: Annotated[int, Path(..., title='id поста', ge=1, lt=100)]) -> Post:
#     for post in posts:
#         if post.id == id:
#             return post
#     raise HTTPException(status_code=404, detail='Post not found')


# @app.get('/search')
# async def search(post_id: Annotated[
#     Optional[int],
#     Query(title='Id of post to search', ge=1, le=50)
# ]) -> dict[str, Optional[Post]]:
#     if post_id:
#         for post in posts:
#             if post.id == post_id:
#                 return {'data': post}
#         raise HTTPException(status_code=404, detail='Post not found')
#     else:
#         return {'data': None}


# @app.post('/user/add')
# async def add_user(user: Annotated[
#     UserCreate,
#     Body(..., example={'name': "UserName", 'age': 120})
# ]) -> User:
#     new_user_id = len(users) + 1
#     if not check_user(user.name, users):
#         raise HTTPException(status_code=400, detail='User with name already have.')
#     new_user = {'id': new_user_id, 'name': user.name, 'age': user.age}
#     users.append(new_user)
#     return User(**new_user)