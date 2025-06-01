from sqlalchemy import Column, String, Integer, Date
from database import Base

class User(Base):
    __tablename__ = "period_tracker_users"
    name= Column(String,nullable=False)
    email = Column(String, primary_key=True, index=True)
    first_period_date = Column(Date, nullable=False)
    cycle_length = Column(Integer, default=28)
