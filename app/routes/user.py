from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas, database

router = APIRouter(prefix="/api/users", tags=["users"])


@router.get("/", response_model=list[schemas.UserOut])
def list_users(db: Session = Depends(database.get_db)):
    return crud.get_all_users(db)

@router.post("/", response_model=schemas.UserOut)
def create_new_user(username:str, password:str, email:str, db:Session = Depends(database.get_db)):
    return crud.create_user(db, username, password, email)


@router.get("/{user_id}", response_model=schemas.UserOut)
def get_user(user_id: int, db: Session = Depends(database.get_db)):
    user = crud.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user



@router.put("/{user_id}", response_model=schemas.UserOut)
def update_user_info(user_id: int, user: schemas.UserUpdate, db: Session = Depends(database.get_db)):
    db_user = crud.get_user_by_id(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    updated_user = crud.update_user(db, user_id, user)
    db.commit()
    db.refresh(updated_user)

    return updated_user


@router.delete("/{user_id}", response_model=dict)
def delete_user_account(user_id: int, db: Session = Depends(database.get_db)):
    db_user = crud.get_user_by_id(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    crud.delete_user(db, user_id)
    return {"message": "User deleted successfully"}