import unittest
from app import create_app, db
from app.models import Notification
from datetime import datetime, timezone
import os
from app.models import Notification
from app.services import NotificationService
service = NotificationService()

class NotificationTestCase(unittest.TestCase):
    """
    Test Notification Model
    We apply principle such as DRY, KISS, YAGNI and, SOLID
    """
    
    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_notification(self):
        notification = self.__new_notification()
        self.assertIsNotNone(notification)
        self.assertEqual(notification.type, 1)
        self.assertEqual(notification.message, "Test message")
    
    def test_save(self):
        notification = self.__new_notification()
        notification_save = service.save(notification)
        self.check_data(notification_save)

    def test_find(self):
        notification = self.__new_notification()
        notification_save = service.save(notification)
        self.check_data(notification_save)
        brand_find = service.find(notification_save.id)
        self.assertIsNotNone(brand_find)

    def test_find_all(self):
        notification = self.__new_notification()
        notification1 = self.__new_notification()
        notification1.message = "Test message 1"
        notification_save = service.save(notification)
        service.save(notification1)
        self.check_data(notification_save)
        notifications = service.find_all()
        self.assertIsNotNone(notifications)
        self.assertEqual(len(notifications), 2)

    def test_find_by_id(self):
        notification = self.__new_notification()
        notification_save = service.save(notification)
        self.check_data(notification_save)
        notification_find_by = service.find_by(id = 1)
        self.assertIsNotNone(notification_find_by)

    def test_update(self):
        notification = self.__new_notification()
        notification_save = service.save(notification)
        notification_save.message = "Updated message"
        notification_update = service.save(notification_save)
        self.assertEqual(notification_update.message, "Updated message")
        self.assertEqual(notification_save.message, notification_update.message)
        self.assertEqual(notification.message, notification_update.message)

    def test_delete(self):
        notification = self.__new_notification()
        notification_save = service.save(notification)
        self.check_data(notification_save)
        notification_delete = service.delete(notification_save)
        self.assertIsNone(notification_delete)
        
    def __new_notification(self):
        notification = Notification()
        notification.type=1
        notification.message="Test message"
        return notification
    
    def check_data(self, save):
        self.assertIsNotNone(save)
        self.assertIsNotNone(save.id)
        self.assertGreater(save.id, 0)

if __name__ == '__main__':
    unittest.main()
