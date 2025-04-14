from typing import List
from app.models import ReceiptType
from app.repositories import ReceiptTypeRepositories
receipt_type_repositories = ReceiptTypeRepositories()

class ReceiptTypeService:
    def save(self, receipt_type: ReceiptType) -> ReceiptType:
        receipt_type_repositories.save(receipt_type)
        return receipt_type
    
    def delete(self, receipt_type: ReceiptType) -> None:
        receipt_type_repositories.delete(receipt_type)

    def find(self, id: int) -> 'ReceiptType':
        return receipt_type_repositories.find(id)
    
    def find_all(self) -> List['ReceiptType']:
        return receipt_type_repositories.find_all()
    
    def find_by(self, **kwargs) -> List['ReceiptType']:
        return receipt_type_repositories.find_by(**kwargs)
    
    