from dataclasses import dataclass
from app import db
from datetime import datetime, timezone

@dataclass
class Notification(db.Model):
    """"
    Model Notification with is attribute
    """
    __tablename__ = 'notifications'
    
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type: int = db.Column(db.Integer, nullable=False) # 1: Info, 2: Warning, 3: Error
    message: str = db.Column(db.String(255), nullable=False)
    date: datetime = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)

