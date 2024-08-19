from fastapi import FastAPI



app = FastAPI()

@app.get("/")
def Home():
    return {"message": "Welcome to the Simple API"}