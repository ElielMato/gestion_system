from dataclasses import dataclass
from app import db

@dataclass(init=True, eq=True)
class ReceiptType(db.Model):
    """
    Model ReceiptType with is attribute
    """
    __tablename__ = 'receipt_types'
    id: int = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column('name', db.String(100), nullable=False)
    description: str = db.Column('description', db.String(150), nullable=True)
    entry: int = db.Column('entry', db.Integer, nullable=False)