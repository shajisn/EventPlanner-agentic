from fastapi import APIRouter, HTTPException, Depends
from typing import List
from app.models.event import Event
from app.schemas.event import Event as EventSchema
from app.db.session import get_db_session

router = APIRouter()

@router.post("/", response_model=EventSchema)
async def create_event(event: EventSchema, db: Session = Depends(get_db_session)):
    db_event = Event(**event.dict())
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event

@router.get("/", response_model=List[EventSchema])
async def get_events(db: Session = Depends(get_db_session)):
    return db.query(Event).all()

@router.get("/{event_id}", response_model=EventSchema)
async def get_event(event_id: int, db: Session = Depends(get_db_session)):
    event = db.query(Event).filter(Event.id == event_id).first()
    if event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return event

@router.put("/{event_id}", response_model=EventSchema)
async def update_event(event_id: int, event: EventSchema, db: Session = Depends(get_db_session)):
    db_event = db.query(Event).filter(Event.id == event_id).first()
    if db_event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    
    for key, value in event.dict().items():
        setattr(db_event, key, value)
    
    db.commit()
    db.refresh(db_event)
    return db_event

@router.delete("/{event_id}", response_model=dict)
async def delete_event(event_id: int, db: Session = Depends(get_db_session)):
    db_event = db.query(Event).filter(Event.id == event_id).first()
    if db_event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    
    db.delete(db_event)
    db.commit()
    return {"status": "success", "message": "Event deleted successfully"}