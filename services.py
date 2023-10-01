from sqlalchemy.orm import Session
import models, schemas

def create_todo(db: Session, todo: schemas.ToDoRequest):
    db_todo = models.ToDo(title=todo.title, completed=todo.completed, priority=todo.priority)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


def read_todos(db: Session, completed: bool, search_string: str = None, sort_order: str = "asc"):
   
    query = db.query(models.ToDo)
     
    if completed is not None:
        query = query.filter(models.ToDo.completed == completed)

    if sort_order.lower() == "asc":
        query = query.order_by(models.ToDo.priority)
    elif sort_order.lower() == "dsc":
        query = query.order_by(models.ToDo.priority.desc())
    
    if search_string:
        query = query.filter(models.ToDo.title.like(f"%{search_string}%"))
    todos = query.all()

    return todos


def update_todo(db: Session, id: int, todo: schemas.ToDoRequest):
    db_todo = db.query(models.ToDo).filter(models.ToDo.id == id).first()
    if db_todo is None:
        return None
    db.query(models.ToDo).filter(models.ToDo.id == id).update({'title': todo.title, 'completed': todo.completed})
    db.commit()
    db.refresh(db_todo)
    return db_todo


def delete_todo(db: Session, id: int):
    db_todo = db.query(models.ToDo).filter(models.ToDo.id == id).first()
    if db_todo is None:
        return None
    db.query(models.ToDo).filter(models.ToDo.id == id).delete()
    db.commit()
    return True