from dataclasses import dataclass
from app import db
from app.models import Article, Batch

@dataclass(init=True, eq=True)
class Stock(db.Model):
    """
    Model Stock with its attributes
    """
    __tablename__ = 'stocks'
    id: int = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    article_id: int = db.Column('article_id', db.Integer, db.ForeignKey('articles.id'), nullable=False)
    # article: Article = db.relationship('Article', back_populates='stock')
    quantity: float = db.Column('quantity', db.Float, nullable=False)
    #batch_id: int = db.Column('batch_id', db.Integer, db.ForeignKey('batches.id'), nullable=False)
    # batch: Batch = db.relationship('Batch', back_populates='stock')
    entry: int = db.Column('entry', db.Integer, nullable=False)  # 1: In, 0: Transfer, -1: Out
    receipt_number: int = db.Column('receipt_number', db.Integer, nullable=False)

    def __eq__(self, stock: object) -> bool:
        return self.id == stock.id