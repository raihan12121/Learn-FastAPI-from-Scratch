from sqlalchemy import false
from fastapi import FastAPI, HTTPException, status, Response, Depends
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from . import models, schemas
from sqlalchemy.orm import Session
from . database import engine, get_db
from typing import List



app = FastAPI()


models.Base.metadata.create_all(bind=engine)




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


# @app.post("/post")
# def create_post(post: Course):
#     cursor.execute("""INSERT INTO courses(name,instructor, duration, website, id) VALUES(%s, %s, %s, %s, %s)RETURNING *""", (post.name, post.instructor, post.duration, str(post.website), post.id))
#     new_post = cursor.fetchone()
#     conn.commit()
#     return{"data": new_post}

@app.post("/courses", response_model=schemas.CourseResponse)
def create_courses(course: schemas.CourseCreate, db: Session = Depends(get_db)):
    new_course = models.Course(**course.model_dump(mode='json'))

    db.add(new_course)
    db.commit()
    db.refresh(new_course)
    return new_course




@app.get("/")
def RaihanApi():
    cursor.execute("""SELECT * FROM courses""")
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
    cursor.execute("""SELECT * FROM courses WHERE id = %s """,(str(id),))
    course = cursor.fetchone()
    if not course:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail= f"Course with id:{id} was not found"
        )
    return{"Course_detail" : course}


@app.get("/coursealchemy/{id}", response_model= List[schemas.CourseResponse])
def Raihan_course(id:int, db: Session = Depends(get_db)):
    course = db.query(models.Course).filter(models.Course.id == id).first()
    if not course:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail= f"Course with id:{id} was not found"
        )
    return course


@app.delete("/course/{id}", status_code = status.HTTP_204_NO_CONTENT)
def delete_course(id: int):
    cursor.execute("""DELETE FROM courses WHERE id = %s returning * """, (str(id),))
    deleted_course = cursor.fetchone()
    conn.commit()
    if deleted_course == None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
        detail= f"course with id; {id} does not exist")
    return Response(status_code=status.HTTP_404_NOT_FOUND)




@app.delete("/Raihan_course_delete/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_Raihan_course(id:int, db:Session=Depends(get_db)):
    course_query = db.query(models.Course).filter(models.Course.id==id)
    course=course_query.first()
    if not course:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"course with id:{id} does not exist")
    course_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/course/{id}")
def update_course(id: int, course: schemas.CourseCreate):
    cursor.execute("""UPDATE courses SET name=%s, instructor=%s, duration = %s, website = %s WHERE id = %s RETURNING * """, (course.name, course.instructor, course.duration, str(course.website), str(id),))
    updated_course = cursor.fetchone()
    conn.commit()

    if updated_course == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail = f"course with id; {id} does not exist")
    return {"data": updated_course}





@app.get("/coursealchemy", response_model= List[schemas.CourseResponse])
def course(db:Session =  Depends(get_db)):
    course = db.query(models.Course).all()
    return{course}


@app.put("/Raihan_course/{id}", response_model= schemas.CourseResponse)
def update_Raihan_course(id:int, updated_course: schemas.CourseCreate, db:Session= Depends(get_db)):
    course_query = db.query(models.Course).filter(models.Course.id==id)
    course = course_query.first()
    if not course:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"course with id: {id} does not exist")
    update_data = updated_course.model_dump()
    update_data["website"] = str(update_data["website"])
    course_query.update(update_data, synchronize_session=False)
    db.commit()
    db.refresh(course)
    return course





@app.post("/users", status_code=status.HTTP_201_CREATED, response_model=schemas.UserRes)
def Raihan_user(user: schemas.UserCreate, db:Session= Depends(get_db)):
    new_user = models.User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user






