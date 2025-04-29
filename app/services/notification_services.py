from typing import List
from app.models import Notification
from app.repositories import NotificationRepository

class NotificationService:
    
    @staticmethod
    def save(notification:Notification) -> Notification:
        NotificationRepository.save(notification)
        return notification
    
    @staticmethod
    def delete(notification:Notification) -> None:
        NotificationRepository.delete(notification)

    @staticmethod
    def find(id: int) -> 'Notification':
        return NotificationRepository.find(id)

    @staticmethod
    def find_all() -> List['Notification']:
        return NotificationRepository.find_all()
    
    @staticmethod
    def find_by(**kwargs) -> List['Notification']:
        return NotificationRepository.find_by(**kwargs)
