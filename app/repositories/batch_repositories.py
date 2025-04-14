from typing import List
from app.models import Batch
from app import db

class BatchRepositories():
    
    def save(self, batch: Batch) -> 'Batch':
        db.session.add(batch)
        db.session.commit()
        return batch
    
    def delete(self, batch: Batch) -> None:
        db.session.delete(batch)
        db.session.commit()

    def find(self, id: int) -> 'Batch':
        return Batch.query.get(id)
    
    def find_all(self) -> List[Batch]:
        return Batch.query.all()
    
    def find_by(self, **kwargs) -> List[Batch]:
        return Batch.query.filter_by(**kwargs).all()