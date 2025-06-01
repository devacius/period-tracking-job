from datetime import date, timedelta
from sqlalchemy.orm import Session
from database import SessionLocal
from models import User

db: Session = SessionLocal()
today = date.today()

# Add a user whose next period is tomorrow
db.add(User(
    name="Fertile Test",
    email="fertile@example.com",
    first_period_date=today - timedelta(days=27),  # 28-day cycle, period tomorrow
    cycle_length=28
))

# Add a user currently in fertile window
db.add(User(
    name="Fertile Window",
    email="fertile.window@example.com",
    first_period_date=today + timedelta(days=14),  # ovulation 14 days before next
    cycle_length=28
))

db.commit()
db.close()
