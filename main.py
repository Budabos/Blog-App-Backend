from fastapi import FastAPI
# Importing BaseModel from Pydantic
from pydantic import BaseModel

class Blog(BaseModel):
    id: int
    title: str
    category: str
    subCategory: str
    description: str
    authorName: str
    authorAvatar: str
    createdAt: datetime
    cover: str
    
        
    

app = FastAPI()

# Define a routes
@app.get("/")
def index():
    return {"message": "Hello, World!"}
