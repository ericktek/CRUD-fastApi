from fastapi import FastAPI
from . import models
from .database import engine
from .routers import users, blogs

# Create all tables in the database
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get('/')

# health check
def read_root():
    return {"message": "Health check successfully!"}

# Register the routers
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(blogs.router, prefix="/blogs", tags=["Blogs"])
