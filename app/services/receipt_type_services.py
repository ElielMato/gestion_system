from typing import List
from app.models import ReceiptType
from app.repositories import ReceiptTypeRepositories
receipt_type_repositories = ReceiptTypeRepositories()

class ReceiptTypeService:
    def save(receipt_type: ReceiptType) -> ReceiptType:
        receipt_type_repositories.save(receipt_type)
        return receipt_type
    
    def find(id: int) -> 'ReceiptType':
        return receipt_type_repositories.find(id)
    
    def find_all() -> List['ReceiptType']:
        return receipt_type_repositories.find_all()
    
    def find_by(**kwargs) -> List['ReceiptType']:
        return receipt_type_repositories.find_by(**kwargs)
    
    