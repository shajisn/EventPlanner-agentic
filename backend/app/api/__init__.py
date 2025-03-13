from fastapi import APIRouter

router = APIRouter()

from .endpoints import events, guests, login, tasks

router.include_router(events.router, prefix="/events", tags=["events"])
router.include_router(guests.router, prefix="/guests", tags=["guests"])
router.include_router(login.router, prefix="/login", tags=["login"])
router.include_router(tasks.router, prefix="/tasks", tags=["tasks"])