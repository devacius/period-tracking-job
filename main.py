from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import scheduler
import models, schemas, crud
from database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)
app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.on_event("startup")
def startup_event():
    scheduler.start()

@app.get("/test-cron")
def test_cron_job():
    scheduler.check_and_notify()
    return {"message": "Cron job executed manually"}

@app.post("/user", response_model=schemas.UserCreate)
def add_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="User already exists")
    return crud.create_user(db, user)

@app.get("/user/{email}", response_model=schemas.PeriodPrediction)
def get_prediction(email: str, db: Session = Depends(get_db)):
    user = crud.get_user(db, email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.predict_period(user)

@app.delete("/user/{email}")
def remove_user(email: str, db: Session = Depends(get_db)):
    if not crud.delete_user(db, email):
        raise HTTPException(status_code=404, detail="User not found")
    return {"detail": "User deleted successfully"}
