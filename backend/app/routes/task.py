from fastapi import APIRouter, Depends
from app.schemas import TaskSchema, UpdateTaskSchema
from app.services import create_task, get_tasks, update_task, delete_task
from app.routes.auth import get_current_user

router = APIRouter(prefix="/task")

@router.post("/create")
def create(data: TaskSchema, user=Depends(get_current_user)):
    return create_task(data, user)

@router.get("/{project_id}")
def get(project_id: str, user=Depends(get_current_user)):
    return get_tasks(project_id, user)

@router.put("/update/{task_id}")
def update(task_id: str, data: UpdateTaskSchema):
    return update_task(task_id, data)

@router.delete("/delete/{task_id}")
def delete(task_id: str):
    return delete_task(task_id)