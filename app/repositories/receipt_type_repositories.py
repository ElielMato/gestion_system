from app import db
from app.models import ReceiptType
from app.repositories import CreateAbstractRepositories, ReadAbstractRepositories, DeleteAbstractRepositories

class ReceiptTypeRepositories(CreateAbstractRepositories, ReadAbstractRepositories, DeleteAbstractRepositories):
    
    def save(self, receipt_type: ReceiptType) -> ReceiptType:
        db.session.add(receipt_type)
        db.session.commit()
        return receipt_type
    
    def delete(self, receipt_type: ReceiptType) -> None:    
        db.session.delete(receipt_type)
        db.session.commit()

    def find(self, id: int) -> 'ReceiptType':
        return ReceiptType.query.get(id)
    
    def find_all(self) -> list:
        return ReceiptType.query.all()
    
    def find_by(self, **kwargs) -> list:
        return ReceiptType.query.filter_by(**kwargs).all()