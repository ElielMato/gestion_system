from dataclasses import dataclass
from app import db
from app.models import Receipt, Article
    
@dataclass(init=True, eq=True)
class ReceiptItem(db.Model):
    """
    Model ReceiptItem with is attribute
    """
    __tablename__ = 'receipt_items'
    id: int = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    article_id: int = db.Column('id_article', db.Integer, db.ForeignKey('articles.id'), nullable=False)
    article: Article = db.relationship('Article', back_populates='receipt_items', lazy=True)
    quantity: float = db.Column('quantity', db.Float, nullable=False)
    batch: str = db.Column('batch', db.String[100], nullable=True)
    receipt = db.relationship('Receipt', back_populates='items', lazy=True) 
    receipt_id: int = db.Column('id_receipt', db.Integer, db.ForeignKey('receipts.id'), nullable=False)