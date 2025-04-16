from typing import List
from app.models import Batch
from app import db
from app.repositories import CreateAbstractRepositories, ReadAbstractRepositories, DeleteAbstractRepositories

class BatchRepositories(CreateAbstractRepositories, ReadAbstractRepositories, DeleteAbstractRepositories):
    
    @staticmethod
    def save(batch: Batch) -> 'Batch':
        db.session.add(batch)
        db.session.commit()
        return batch
    
    @staticmethod
    def delete(batch: Batch) -> None:
        db.session.delete(batch)
        db.session.commit()

    @staticmethod
    def find(id: int) -> 'Batch':
        return Batch.query.get(id)
    
    @staticmethod
    def find_all() -> List[Batch]:
        return Batch.query.all()
    
    @staticmethod
    def find_by(**kwargs) -> List[Batch]:
        return Batch.query.filter_by(**kwargs).all()