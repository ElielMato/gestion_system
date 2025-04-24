from dataclasses import dataclass
from app import db
from app.models import Receipt, Article
from sqlalchemy.orm import Mapped
    
@dataclass(init=True, eq=True)
class ReceiptItem(db.Model):
    """
    Model ReceiptItem with is attribute
    """
    __tablename__ = 'receipt_items'
    id: int = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    quantity: int = db.Column('quantity', db.Float, nullable=False, default=0)

    article_id: int = db.Column('article_id', db.Integer, db.ForeignKey('articles.id'), nullable=False)
    article = db.relationship(Article)

    batch_id: int = db.Column('batch_id', db.Integer, db.ForeignKey('batchs.id'), nullable=False)
    batch = db.relationship('Batch')

    receipt_id: int = db.Column('id_receipt', db.Integer, db.ForeignKey('receipts.id'), nullable=False)
    receipt = db.relationship(Receipt)