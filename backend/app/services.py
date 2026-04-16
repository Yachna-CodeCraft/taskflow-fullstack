from app.database import db
from app.security import hash_password, verify_password, create_token
from bson import ObjectId

# AUTH
def register_user(data):
    if db.users.find_one({"email": data.email}):
        return {"error": "User exists"}

    db.users.insert_one({
        "email": data.email,
        "password": hash_password(data.password)
    })

    return {"message": "Registered"}

def login_user(data):
    user = db.users.find_one({"email": data.email})
    if not user:
        return {"error": "User not found"}

    if not verify_password(data.password, user["password"]):
        return {"error": "Wrong password"}

    token = create_token({"email": user["email"]})
    return {"access_token": token}


# PROJECT
def create_project(data, user):
    db.projects.insert_one({
        "name": data.name,
        "user_email": user["email"]
    })
    return {"message": "Project created"}

def get_projects(user):
    projects = list(db.projects.find({"user_email": user["email"]}))
    for p in projects:
        p["_id"] = str(p["_id"])
    return projects


# TASK
def create_task(data, user):
    db.tasks.insert_one({
        "title": data.title,
        "project_id": data.project_id,
        "user_email": user["email"],
        "status": "Todo"
    })
    return {"message": "Task created"}

def get_tasks(project_id, user):
    tasks = list(db.tasks.find({
        "project_id": project_id,
        "user_email": user["email"]
    }))
    for t in tasks:
        t["_id"] = str(t["_id"])
    return tasks

def update_task(task_id, data):
    db.tasks.update_one(
        {"_id": ObjectId(task_id)},
        {"$set": {"status": data.status}}
    )
    return {"message": "Task updated"}

def delete_task(task_id):
    db.tasks.delete_one({"_id": ObjectId(task_id)})
    return {"message": "Task deleted"}