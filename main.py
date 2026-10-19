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
    id: int


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
    cursor.execute("""INSERT INTO course(name,instructor, duration, website, id) VALUES(%s, %s, %s, %s, %s)RETURNING *""", (post.name, post.instructor, post.duration, str(post.website), post.id))
    new_post = cursor.fetchone()
    conn.commit()
    return{"data": new_post}


@app.get("/")
def RaihanApi():
    cursor.execute("""SELECT * FROM course""")
    data = cursor.fetchall()
    return {"Data" : data}

@app.get("/course")
def FastapiCourse():
    return {"Course": "FastAPI & Backend API development with Python"}


@app.get("/Career/AI Engineer")
def Career():
    return {"Career": "Raihan Wants to be Ai engineer so much"}