from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl
import psycopg2
from psycopg2.extras import RealDictCursor
import time



app = FastAPI()


#define request body Shcema
class  Course(BaseModel):
    name : str
    instructor: str
    duration: float
    website: HttpUrl


while True:
    try:
        conn = psycopg2.connect(host = 'localhost', database='Raihan', user = 'postgres',
        password ='12345', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print('Successfully connected Database')
        break 
    except Exception as error:
        print('Database connection Failed')
        print("error:", error)
        time.sleep(2)


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