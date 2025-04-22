from dataclasses import dataclass
from app import db
from sqlalchemy.orm import Mapped

@dataclass(init=True, eq=True)
class Stock(db.Model):
    __tablename__ = 'stock'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    article_id: int = db.Column('article_id', db.Integer, db.ForeignKey('articles.id'), nullable=False)
    # article: Mapped["Article"] = db.relationship('Article', back_populates='receipt_items', lazy=True)
    quantity = db.Column(db.Integer, nullable=False, default=0)
    batch_id: int = db.Column('batch_id', db.Integer, db.ForeignKey('batchs.id'), nullable=False)
    # batch: Mapped["Batch"] = db.relationship('Batch', lazy=True)
   
    def __eq__(self, stock: object) -> bool:
        return self.id == stock.id