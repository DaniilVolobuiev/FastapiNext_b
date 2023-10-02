from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status
import schemas
import services
from database import SessionLocal

router = APIRouter(
    prefix="/todos"
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("", status_code=status.HTTP_201_CREATED)
def create_todo(todo: schemas.ToDoRequest, db: Session = Depends(get_db)):
    todo = services.create_todo(db, todo)
    return todo


@router.get("", response_model=List[schemas.ToDoResponse])
def get_todos(completed: bool = None, search_string: str = None, db: Session = Depends(get_db), sort_order: str = "asc"):
    todos = services.read_todos(db, completed, search_string, sort_order)
     
    return todos


@router.put("/{id}")
def update_todo(id: int, todo: schemas.ToDoUpdateRequest, db: Session = Depends(get_db)):
    todo = services.update_todo(db, id, todo)
    if todo is None:
        raise HTTPException(status_code=404, detail="to do not found")
    
    return todo


@router.delete("/{id}", status_code=status.HTTP_200_OK)
def delete_todo(id: int, db: Session = Depends(get_db)):
    res = services.delete_todo(db, id)
    if res is None:
        raise HTTPException(status_code=404, detail="to do not found")