from typing import List
from app.models import Notification
from app.repositories import NotificationRepositories
notification_repositories = NotificationRepositories()

class NotificationService:
    def save(notification:Notification) -> Notification:
        notification_repositories.save(notification)
        return notification
    
    def delete(notification:Notification) -> None:
        notification_repositories.delete(notification)

    def find(id: int) -> 'Notification':
        return notification_repositories.find(id)

    def find_all() -> List['Notification']:
        return notification_repositories.find_all()
    
    def find_by(**kwargs) -> List['Notification']:
        return notification_repositories.find_by(**kwargs)
