from sqlalchemy.orm import Session
from . import models, schemas
from passlib.context import CryptContext 

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_user_by_email(db: Session, email: str):
    """Retrieve a user by their email address."""
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
    """Create a new user with hashed password."""
    hashed_password = pwd_context.hash(user.password)
    db_user = models.User(name=user.name, email=user.email, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_blog_post(db: Session, blog_post: schemas.BlogPostCreate, user_id: int):
    """Create a new blog post."""
    db_blog_post = models.BlogPost(**blog_post.dict(), author_id=user_id)
    db.add(db_blog_post)
    db.commit()
    db.refresh(db_blog_post)
    return db_blog_post

def get_users(db: Session, skip: int = 0, limit: int = 10):
    """Retrieve a list of users."""
    return db.query(models.User).offset(skip).limit(limit).all()

def get_user(db: Session, user_id: int):
    """Retrieve a user by their ID."""
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_blog_posts(db: Session, skip: int = 0, limit: int = 10):
    """Retrieve a list of blog posts."""
    return db.query(models.BlogPost).offset(skip).limit(limit).all()

def get_blog_post(db: Session, blog_post_id: int):
    """Retrieve a blog post by its ID."""
    return db.query(models.BlogPost).filter(models.BlogPost.id == blog_post_id).first()
