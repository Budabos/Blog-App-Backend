from fastapi import FastAPI

app = FastAPI()

# Define a route
@app.get("/")
def index():
    return {"message": "Hello, World!"}
