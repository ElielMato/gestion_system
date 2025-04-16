from abc import ABC, abstractmethod
from typing import List
from app import db

class CreateAbstractRepositories(ABC):

    @abstractmethod
    def save(model:db.Model) -> db.Model:
        pass

class ReadAbstractRepositories(ABC):
    
    @abstractmethod
    def find(id: int) -> 'db.Model':
        pass

    @abstractmethod
    def find_all() -> List['db.Model']:
        pass
    
    @abstractmethod
    def find_by(**kwargs) -> List['db.Model']:
        pass

class UpdateAbstractRepositories(ABC):

    @abstractmethod
    def update(id: int, model:db.Model) -> db.Model:
        pass

class DeleteAbstractRepositories(ABC):
    
    @abstractmethod
    def delete(model:db.Model) -> None:
        pass