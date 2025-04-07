from abc import ABC, abstractmethod
from typing import List
from app import db

class CreateAbstractRepositories(ABC):

    @abstractmethod
    def save(self, model:db.Model) -> db.Model:
        pass

class ReadAbstractRepositories(ABC):
    
    @abstractmethod
    def find(self, id: int) -> 'db.Model':
        pass

    @abstractmethod
    def find_all(self) -> List['db.Model']:
        pass
    
    @abstractmethod
    def find_by(self, **kwargs) -> List['db.Model']:
        pass

class UpdateAbstractRepositories(ABC):

    @abstractmethod
    def update(self, id: int, model:db.Model) -> db.Model:
        pass

class DeleteAbstractRepositories(ABC):
    
    @abstractmethod
    def delete(self, model:db.Model) -> None:
        pass