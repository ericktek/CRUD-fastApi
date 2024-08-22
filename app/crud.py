from sqlalchemy.orm import Session
from . import models, schemas
from passlib.context import CryptContext 

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Retrieve a user by their email address. 
def get_user_by_email(db: Session, email: str):
    """Retrieve a user by their email address."""
    return db.query(models.User).filter(models.User.email == email).first()

# create a new user with hashed password. 
def create_user(db: Session, user: schemas.UserCreate):
    """Create a new user with hashed password."""
    hashed_password = pwd_context.hash(user.password)
    db_user = models.User(name=user.name, email=user.email, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# create a new blog post. 
def create_blog_post(db: Session, blog_post: schemas.BlogPostCreate, user_id: int):
    """Create a new blog post."""
    db_blog_post = models.BlogPost(**blog_post.model_dump(), author_id=user_id)
    db.add(db_blog_post)
    db.commit()
    db.refresh(db_blog_post)
    return db_blog_post

#  Retrieve a list of users. 
def get_users(db: Session, skip: int = 0, limit: int = 10):
    """Retrieve a list of users."""
    return db.query(models.User).offset(skip).limit(limit).all()

#  Retrieve a user by their ID. 
def get_user(db: Session, user_id: int):
    """Retrieve a user by their ID."""
    return db.query(models.User).filter(models.User.id == user_id).first()

#  Retrieve a list of blog posts. 
def get_blog_posts(db: Session, skip: int = 0, limit: int = 10):
    """Retrieve a list of blog posts."""
    return db.query(models.BlogPost).offset(skip).limit(limit).all()

#  Retrieve a blog post by its ID. 
def get_blog_post(db: Session, blog_post_id: int):
    """Retrieve a blog post by its ID."""
    return db.query(models.BlogPost).filter(models.BlogPost.id == blog_post_id).first()

#  Update a blog post.
def update_blog_post(db: Session, blog_post_id: int, blog_post: schemas.BlogPostUpdate):
    db_blog_post = get_blog_post(db, blog_post_id=blog_post_id)
    if db_blog_post:
        for key, value in blog_post.dict().items():
            setattr(db_blog_post, key, value)
        db.commit()
        db.refresh(db_blog_post)
    return db_blog_post

#  Delete a blog post.
def delete_blog_post(db: Session, blog_post_id: int):
    db_blog_post = get_blog_post(db, blog_post_id=blog_post_id)
    if db_blog_post:
        db.delete(db_blog_post)
        db.commit()

# Update a user. 
def update_user(db: Session, user_id: int, user: schemas.UserUpdate):
    db_user = get_user(db, user_id=user_id)
    if db_user:
        for key, value in user.model_dump().items():
            setattr(db_user, key, value)
        db.commit()
        db.refresh(db_user)
    return db_user

# Delete a user. 
def delete_user(db: Session, user_id: int):
    db_user = get_user(db, user_id=user_id)
    if db_user:
        db.delete(db_user)
        db.commit()
