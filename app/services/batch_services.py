from typing import List
from app.models import Batch
from app.repositories import BatchRepositories
batch_repositories = BatchRepositories()


class BatchService():
    
    def save(batch: Batch) -> 'Batch':
        batch_repositories.save(batch)
        return batch
    
    def delete(batch: 'Batch') -> None:
        batch_repositories.delete(batch)

    def find(id: int) -> 'Batch':
        return batch_repositories.find(id)
    
    def find_all() -> List['Batch']:
        return batch_repositories.find_all()
    
    def find_by(**kwargs) -> List['Batch']:
        return batch_repositories.find_by(**kwargs)