from fastapi import APIRouter, Depends
from app.schemas import ProjectSchema
from app.services import create_project, get_projects
from app.routes.auth import get_current_user

router = APIRouter(prefix="/project")

@router.post("/create")
def create(data: ProjectSchema, user=Depends(get_current_user)):
    return create_project(data, user)

@router.get("/all")
def all(user=Depends(get_current_user)):
    return get_projects(user)