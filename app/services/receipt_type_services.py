from typing import List
from app.models import ReceiptType
from app.repositories import ReceiptTypeRepository

class ReceiptTypeService:

    @staticmethod
    def save(receipt_type: ReceiptType) -> ReceiptType:
        ReceiptTypeRepository.save(receipt_type)
        return receipt_type
    
    @staticmethod
    def find(id: int) -> 'ReceiptType':
        receipt_type = ReceiptTypeRepository.find(id)
        if not receipt_type:
                raise ValueError(f"Receipt type with ID {id} not found.")
        return receipt_type
    
    @staticmethod
    def find_all() -> List['ReceiptType']:
        return ReceiptTypeRepository.find_all()
    
    @staticmethod
    def find_by(**kwargs) -> List['ReceiptType']:
        return ReceiptTypeRepository.find_by(**kwargs)
    
    