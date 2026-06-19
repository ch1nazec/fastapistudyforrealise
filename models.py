from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import mapped_column, relationship, Mapped
from database import Base


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(unique=True, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, index=True)
    age: Mapped[int] = mapped_column(Integer)

    posts = relationship("Post", back_populates="author", lazy="selectin")


class Post(Base):
    __tablename__ = 'posts'

    id: Mapped[int] = mapped_column(unique=True, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String, index=True)
    body: Mapped[str] = mapped_column(String)

    author_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'))
    author = relationship("User", back_populates="posts", lazy="joined")