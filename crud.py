# STEP 6 — crud.py (Database Logic)
from sqlalchemy.orm import Session
from models import User
from schemas import UserCreate, UserLogin, UserResponse
from auth import hash_password

# def create_user(db: Session, user: schemas.UserCreate):
#     db_user = models.User(name=user.name, email=user.email, password=user.password)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user

def create_user(db: Session, user: UserCreate):
    hashed_pwd = hash_password(user.password)
    print("Incoming password:", user.password)
    print("Length:", len(user.password))

    db_user = User(
        name=user.name,
        email=user.email,
        hashed_password=hashed_pwd
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session):
    return db.query(User).all()

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def update_user(db: Session, user_id: int, user: UserCreate):
    db_user = get_user(db, user_id)
    if db_user:
        db_user.name = user.name
        db_user.email = user.email
        db_user.hashed_password = hash_password(user.password)
        db.commit()
        db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = get_user(db, user_id)
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user