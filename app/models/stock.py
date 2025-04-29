from dataclasses import dataclass
from app import db
from sqlalchemy.orm import Mapped

@dataclass(init=True, eq=True)
class Stock(db.Model):
    
    __tablename__ = 'stock'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    id_article: int = db.Column('id_article', db.Integer, db.ForeignKey('articles.id'), nullable=False)
    id_batch: int = db.Column('id_batch', db.Integer, db.ForeignKey('batches.id'), nullable=False)
    id_receipt: int = db.Column('id_receipt', db.Integer, db.ForeignKey('receipts.id'), nullable=True)
    quantity = db.Column(db.Integer, nullable=False, default=0)
    
    article = db.relationship('Article', lazy=True)
    batch = db.relationship('Batch', lazy=True)
    receipt = db.relationship('Receipt', lazy=True) 