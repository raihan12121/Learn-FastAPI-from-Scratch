from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl




app = FastAPI()


#define request body Shcema
class  Course(BaseModel):
    name : str
    instructor: str
    duration: float
    website: HttpUrl


@app.post("/post")
def create_post(post: Course):
    return{"data": post}


@app.get("/")
def RaihanApi():
    return {"Raihan" : "FastAPi"}

@app.get("/course")
def FastapiCourse():
    return {"Course": "FastAPI & Backend API development with Python"}


@app.get("/Career/AI Engineer")
def Career():
    return {"Career": "Raihan Wants to be Ai engineer so much"}