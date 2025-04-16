from typing import List
from app.models import Receipt
from app.repositories import ReceiptRepositories
receipt_repositories = ReceiptRepositories()

class ReceiptService():
    
    def save(self, receipt: Receipt) -> 'Receipt':
        receipt_repositories.save(receipt)
        return receipt
    
    def delete(self, receipt: 'Receipt') -> None:
        receipt_repositories.delete(receipt)

    def find(self, id: int) -> 'Receipt':
        return receipt_repositories.find(id)
    
    def find_all(self) -> List['Receipt']:
        return receipt_repositories.find_all()
    
    def find_by(self, **kwargs) -> List['Receipt']:
        return receipt_repositories.find_by(**kwargs)