from storage import load_users
from datetime import datetime, timedelta, date
from utils import send_email

def check_reminders():
    users = load_users()
    today = date.today()
    
    for user in users:
        last_period = datetime.strptime(user["last_period_start"], "%Y-%m-%d").date()
        next_period = last_period + timedelta(days=user["cycle_length"])
        
        if next_period == today:
            send_email(user["email"], "Period Reminder", "Your period is expected to start today!")

if __name__ == "__main__":
    check_reminders()
