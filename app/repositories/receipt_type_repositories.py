from app import db
from app.models import ReceiptType
from app.repositories import CreateAbstractRepositories, ReadAbstractRepositories

class ReceiptTypeRepositories(CreateAbstractRepositories, ReadAbstractRepositories):
    
    @staticmethod
    def save(receipt_type: ReceiptType) -> ReceiptType:
        db.session.add(receipt_type)
        db.session.commit()
        return receipt_type

    @staticmethod
    def find(id: int) -> 'ReceiptType':
        return ReceiptType.query.get(id)
    
    @staticmethod
    def find_all() -> list:
        return ReceiptType.query.all()
    
    @staticmethod
    def find_by(**kwargs) -> list:
        return ReceiptType.query.filter_by(**kwargs).all()