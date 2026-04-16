from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import auth, project, task

# ✅ 1. create app FIRST
app = FastAPI()

# ✅ 2. then middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ 3. then routes
app.include_router(auth.router)
app.include_router(project.router)
app.include_router(task.router)