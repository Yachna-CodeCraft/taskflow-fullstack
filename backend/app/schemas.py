from pydantic import BaseModel, EmailStr

class RegisterSchema(BaseModel):
    email: EmailStr
    password: str

class LoginSchema(BaseModel):
    email: EmailStr
    password: str

class ProjectSchema(BaseModel):
    name: str

class TaskSchema(BaseModel):
    title: str
    project_id: str

class UpdateTaskSchema(BaseModel):
    status: str