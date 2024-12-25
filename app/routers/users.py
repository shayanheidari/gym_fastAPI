from typing import List, Tuple
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app import models, schemas


router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=schemas.UserOut)
def create_user(
    user: schemas.UserCreate, db: Session = Depends(get_db)
) -> schemas.UserOut:
    # TODO: hash the password
    new_user = models.User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/", response_model=List[schemas.UserOut])
def get_users(db: Session = Depends(get_db)) -> schemas.UserOut:
    users = db.query(models.User).all()
    if not users:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            detail="no users was found.")
    return users


@router.get("/{id}", response_model=schemas.UserOut)
def get_user(id: int, db: Session = Depends(get_db)) -> schemas.UserOut:
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail=f"no users was found with id = {
                id}.",
        )
    return user
