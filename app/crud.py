from sqlalchemy.orm import Session
from app.models import User
from app.schemas import UserCreate, UserUpdate

def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id, User.is_deleted == False).first()


def get_all_users(db: Session):
    return db.query(User).filter(User.is_deleted == False).all()


def create_user(db: Session, username, password, email):
    db_user = User(
        username=username,
        email=email,
        password=password,
        is_deleted=False
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, user_id: int, user: UserUpdate):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        return None

    for key, value in user.dict(exclude_unset=True).items():
        setattr(db_user, key, value)

    return db_user

def delete_user(db: Session, user_id: int):
    user = get_user_by_id(db, user_id)
    if user:
        user.is_deleted = True
        db.commit()


