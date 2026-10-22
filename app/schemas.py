from datetime import datetime
from pydantic import BaseModel, HttpUrl, ConfigDict, EmailStr



class CourseCreate(BaseModel):
    name : str
    instructor: str
    duration: float
    website: HttpUrl
    id: int



class CourseResponse(CourseCreate):
    id : int
    model_config = ConfigDict(from_attributes=True)




class UserCreate(BaseModel):
    email : EmailStr
    password : str


class UserRes(BaseModel):
    id: int
    email: EmailStr
    created_at : datetime
    model_config = ConfigDict(from_attributes=True)



class UserLogin(BaseModel):
    email : EmailStr
    password : str