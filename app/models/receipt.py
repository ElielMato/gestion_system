from dataclasses import dataclass
from datetime import datetime
from app import db
from sqlalchemy.orm import Mapped, mapped_column, relationship

@dataclass(init=True, eq=True)
class ReceiptType(db.Model):
    """
    Model ReceiptType with is attribute
    """
    __tablename__ = 'receipt_types'
    __table_args__ = {'extend_existing': True}  # Permite extender la tabla existente
    id: int = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column('name', db.String[100], nullable=False)
    description: str = db.Column('description', db.String[150], nullable=True)
    type: int = db.Column('type', db.Integer, nullable=False)
    
@dataclass(init=True, eq=True)
class ReceiptHeader(db.Model):
    """
    Model ReceiptHeader with is attribute
    """
    __tablename__ = 'receipt_headers'
    __table_args__ = {'extend_existing': True}  # Permite extender la tabla existente
    id: int = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    submission_date: datetime = db.Column('submission_date', db.DateTime, nullable=False)

@dataclass(init=True, eq=True)
class ReceiptItem(db.Model):
    """
    Model ReceiptItem with is attribute
    """
    __tablename__ = 'receipt_items'
    __table_args__ = {'extend_existing': True}  # Permite extender la tabla existente
    id: int = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    id_article: list = db.Column('id_article', db.Integer, nullable=False)
    quantity: float = db.Column('quantity', db.Float, nullable=False)
    batch: str = db.Column('batch', db.String[100], nullable=True)

@dataclass(init=True, eq=True)
class ReceiptFooter(db.Model):
    """
    Model ReceiptFooter with is attribute
    """
    __tablename__ = 'receipt_footers'
    __table_args__ = {'extend_existing': True}  # Permite extender la tabla existente
    id: int = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    total: float = db.Column('total', db.Float, nullable=False)

@dataclass(init=True, eq=True)
class Receipt(db.Model):
    """
    Model Receipt with is attribute
    """
    __tablename__ = 'receipts'
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True, autoincrement=True)
    # header: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('receipt_headers.id'), nullable=False)
    # footer: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('receipt_footers.id'), nullable=False)
    # items: Mapped[list[ReceiptItem]] = relationship('ReceiptItem', backref='receipt', lazy=True)
    # receipt_type: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('receipt_types.id'), nullable=False)