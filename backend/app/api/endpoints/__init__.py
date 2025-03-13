# filepath: /event-planner/event-planner/backend/app/api/endpoints/__init__.py
from fastapi import APIRouter

router = APIRouter()

from .login import router as login_router
from .events import router as events_router
from .guests import router as guests_router
from .tasks import router as tasks_router

router.include_router(login_router, prefix="/login", tags=["login"])
router.include_router(events_router, prefix="/events", tags=["events"])
router.include_router(guests_router, prefix="/guests", tags=["guests"])
router.include_router(tasks_router, prefix="/tasks", tags=["tasks"])