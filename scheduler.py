from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from database import SessionLocal
from emails import send_notification_email
from models import User

def check_and_notify():
    db: Session = SessionLocal()
    today = datetime.utcnow().date()

    users = db.query(User).all()
    for user in users:
        cycle_length = user.cycle_length or 28
        last_period = user.first_period_date
        while last_period < today:
            last_period += timedelta(days=cycle_length)

        days_until_next_period = (last_period - today).days
        fertile_start = last_period - timedelta(days=14)
        fertile_end = fertile_start + timedelta(days=5)

        if days_until_next_period == 1:
            send_notification_email(
                f"{user.name}, your period is expected tomorrow",
                f"Hi {user.name}! Just a reminder: period is expected tomorrow. ❤️"
            )
        elif fertile_start <= today <= fertile_end:
            send_notification_email(
                f"{user.name} is in her fertile window",
                f"Hi! {user.name} currently in her fertile window. 🌸"
            )

    db.close()

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(check_and_notify, "cron", hour=8)  # Runs every day at 8 AM UTC
    scheduler.start()
