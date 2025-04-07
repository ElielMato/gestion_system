from typing import List
from app.models import Notification
from app.repositories import NotificationRepositories
notification_repositories = NotificationRepositories()

class NotificationService:
    def save(self, notification:Notification) -> Notification:
        notification_repositories.save(notification)
        return notification
    
    def delete(self, notification:Notification) -> None:
        notification_repositories.delete(notification)

    def find(self, id: int) -> 'Notification':
        return notification_repositories.find(id)

    def find_all(self) -> List['Notification']:
        return notification_repositories.find_all()
    
    def find_by(self, **kwargs) -> List['Notification']:
        return notification_repositories.find_by(**kwargs)
