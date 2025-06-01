from sqlalchemy.orm import Session
from models import User
from schemas import UserCreate, PeriodPrediction
from datetime import timedelta, date

def create_user(db: Session, user: UserCreate):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def delete_user(db: Session, email: str):
    user = get_user(db, email)
    if user:
        db.delete(user)
        db.commit()
        return True
    return False

def predict_period(user: User) -> PeriodPrediction:
    next_period = user.first_period_date + timedelta(days=user.cycle_length)
    fertile_start = next_period - timedelta(days=14)
    fertile_end = fertile_start + timedelta(days=6)
    return PeriodPrediction(
        next_period_start=next_period,
        fertile_window=[fertile_start, fertile_end]
    )
