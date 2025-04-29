from dataclasses import dataclass
from app import db
from datetime import datetime, timezone

@dataclass(init=True, eq=False)
class Batch(db.Model):
    """
    Model Batch with is attribute
    """
    __tablename__ = "batches"
    id: int = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
    code: str = db.Column("code", db.String(100), nullable=False)
    expiration_date: datetime = db.Column("expiration_date", db.DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)