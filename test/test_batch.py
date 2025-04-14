import os
import unittest
from app import create_app
from app import db
from app.models import Batch
from app.services import BatchService
service = BatchService()

class BatchTestCase(unittest.TestCase):
    """
    Test Batch Model
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

    def test_batch(self):
        batch = self.__new_batch()
        self.assertIsNotNone(batch)
        self.assertEqual(batch.code, '1')

    def test_save(self):
        batch = self.__new_batch()
        batch_save = service.save(batch)
        self.check_data(batch_save)

    def test_find(self):
        batch = self.__new_batch()
        batch_save = service.save(batch)
        self.check_data(batch_save)
        batch_find = service.find(batch_save.id)
        self.assertIsNotNone(batch_find)

    def test_find_all(self):
        batch = self.__new_batch()
        batch1 = self.__new_batch()
        batch1.code = '2'
        batch_save = service.save(batch)
        service.save(batch1)
        self.check_data(batch_save)
        batches = service.find_all()
        self.assertIsNotNone(batches)
        self.assertEqual(len(batches), 2)

    def test_find_by(self):
        batch = self.__new_batch()
        batch_save = service.save(batch)
        self.check_data(batch_save)
        batch_find_by = service.find_by(code = '1')
        self.assertIsNotNone(batch_find_by)

    def test_update(self):
        batch = self.__new_batch()
        batch_save = service.save(batch)
        batch_save.code = '4'
        batch_update_save = service.save(batch_save)
        self.assertEqual(batch_update_save.code, '4')
        self.assertEqual(batch_save.code, batch_update_save.code)

    def test_delete(self):
        batch = self.__new_batch()
        batch_save = service.save(batch)
        self.check_data(batch_save)
        batch_delete = service.delete(batch_save)
        self.assertIsNone(batch_delete)

    def __new_batch(self):
        batch = Batch()
        batch.code = '1'
        return batch
    
    def check_data(self, save):
        self.assertIsNotNone(save)
        self.assertIsNotNone(save.id)
        self.assertGreater(save.id, 0)