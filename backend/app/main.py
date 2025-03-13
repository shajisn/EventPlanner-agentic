from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.endpoints import events, guests, login, tasks
from app.db.init_db import init_db

app = FastAPI(
    title="InApp 25th Anniversary API",
    description="API for managing InApp's 25th Anniversary celebration",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

init_db()

app.include_router(events.router, prefix="/api/events", tags=["events"])
app.include_router(guests.router, prefix="/api/guests", tags=["guests"])
app.include_router(login.router, prefix="/api/login", tags=["login"])
app.include_router(tasks.router, prefix="/api/tasks", tags=["tasks"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)