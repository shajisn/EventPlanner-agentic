from fastapi import APIRouter, HTTPException
from typing import List
from app.models.guest import Guest
from app.schemas.guest import Guest as GuestSchema
from app.db.session import get_db_session

router = APIRouter()

@router.get("/", response_model=List[GuestSchema])
async def get_guests():
    db = get_db_session()
    guests = db.query(Guest).all()
    return guests

@router.post("/", response_model=GuestSchema)
async def create_guest(guest: GuestSchema):
    db = get_db_session()
    new_guest = Guest(**guest.dict())
    db.add(new_guest)
    db.commit()
    db.refresh(new_guest)
    return new_guest

@router.put("/{guest_id}", response_model=GuestSchema)
async def update_guest(guest_id: int, guest: GuestSchema):
    db = get_db_session()
    existing_guest = db.query(Guest).filter(Guest.id == guest_id).first()
    
    if not existing_guest:
        raise HTTPException(status_code=404, detail="Guest not found")
    
    for key, value in guest.dict().items():
        setattr(existing_guest, key, value)
    
    db.commit()
    db.refresh(existing_guest)
    return existing_guest

@router.delete("/{guest_id}", response_model=dict)
async def delete_guest(guest_id: int):
    db = get_db_session()
    existing_guest = db.query(Guest).filter(Guest.id == guest_id).first()
    
    if not existing_guest:
        raise HTTPException(status_code=404, detail="Guest not found")
    
    db.delete(existing_guest)
    db.commit()
    return {"status": "success", "message": "Guest deleted successfully"}