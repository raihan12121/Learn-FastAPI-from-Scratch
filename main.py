from fastapi import FastAPI, HTTPException, status,Response
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

@app.get("/CourseName")
def FastapiCourse():
    return {"CourseName": "FastAPI & Backend API development with Python"}


@app.get("/Career/AI Engineer")
def Career():
    return {"Career": "Raihan Wants to be Ai engineer so much"}

@app.get("/course/{id}")
def get_course(id:int):
    cursor.execute("""SELECT * FROM course WHERE id = %s """,(str(id),))
    course = cursor.fetchone()
    if not course:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail= f"Course with id:(id) was not found"
        )
    return{"Course_detail" : course}


@app.delete("/course/{id}", status_code = status.HTTP_204_NO_CONTENT)
def delete_course(id: int):
    cursor.execute("""DELETE FROM course WHERE id = %s returning * """, (str(id),))
    deleted_course = cursor.fetchone()
    conn.commit()
    if deleted_course == None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
        detail= f"course with id; {id} does not exist")
    return Response(status_code=status.HTTP_404_NOT_FOUND)


@app.put("/course/{id}")
def update_course(id: int, course:Course):
    cursor.execute("""UPDATE course SET name=%s, instructor=%s, duration = %s, website = %s WHERE id = %s RETURNING * """, (course.name, course.instructor, course.duration, str(course.website), str(id),))
    updated_course = cursor.fetchone()
    conn.commit()

    if updated_course == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail = f"course with id; {id} does not exist")
    return {"data": updated_course}