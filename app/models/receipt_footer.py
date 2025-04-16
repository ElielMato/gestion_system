from dataclasses import dataclass
from app import db

@dataclass(init=True, eq=True)
class ReceiptFooter(db.Model):
    """
    Model ReceiptFooter with is attribute
    """
    __tablename__ = 'receipt_footers'
    id: int = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    total: float = db.Column('total', db.Float, nullable=False)
