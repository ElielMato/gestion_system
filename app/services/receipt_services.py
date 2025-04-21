from typing import List
from app.models import Receipt
from app.repositories import ReceiptRepositories
receipt_repositories = ReceiptRepositories()

class ReceiptService():
    
    def save(receipt: Receipt) -> 'Receipt':
        receipt_repositories.save(receipt)
        return receipt

    def find(id: int) -> 'Receipt':
        return receipt_repositories.find(id)
    
    def find_all() -> List['Receipt']:
        return receipt_repositories.find_all()
    
    def find_by(**kwargs) -> List['Receipt']:
        return receipt_repositories.find_by(**kwargs)