from typing import List
from app.models import Receipt
from app import db
from app.repositories import CreateAbstractRepository, ReadAbstractRepository

class ReceiptRepository(CreateAbstractRepository, ReadAbstractRepository):
    
    @staticmethod
    def save(receipt: Receipt) -> Receipt:
        db.session.add(receipt)
        db.session.commit()
        return receipt
    
    @staticmethod
    def find(id: int) -> 'Receipt':
        return Receipt.query.get(id)

    @staticmethod
    def find_all() -> List['Receipt']:
        return Receipt.query.all()
    
    @staticmethod
    def find_by(**kwargs) -> List['Receipt']:
        return Receipt.query.filter_by(**kwargs).all()
