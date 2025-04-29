from typing import List
from app.models import Batch
from app.repositories import BatchRepository

class BatchService():
    
    @staticmethod
    def save(batch: Batch) -> 'Batch':
        BatchRepository.save(batch)
        return batch
    
    @staticmethod
    def delete(batch: 'Batch') -> None:
        BatchRepository.delete(batch)

    @staticmethod
    def find(id: int) -> 'Batch':
        return BatchRepository.find(id)
    
    @staticmethod
    def find_all() -> List['Batch']:
        return BatchRepository.find_all()
    
    @staticmethod
    def find_by(**kwargs) -> List['Batch']:
        return BatchRepository.find_by(**kwargs)