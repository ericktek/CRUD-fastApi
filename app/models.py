from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100))
    email = Column(String(100), unique=True, index=True)
    password = Column(String(255))

    blogs = relationship("BlogPost", back_populates="author")

class BlogPost(Base):
    __tablename__ = "blog_posts"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(100))
    description = Column(String(250))
    image = Column(String(100))
    author_id = Column(Integer, ForeignKey("users.id"))

    author = relationship("User", back_populates="blogs")
