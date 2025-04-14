import os
import unittest
from app import create_app
from app import db
from app.models import ReceiptType
from app.services import ReceiptTypeService
service = ReceiptTypeService()

class ReceiptTypeTestCase(unittest.TestCase):
    """
    Test Receipt Type Model
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

    def test_receipt_type(self):
        receipt_type = self.__new_receipt_type()
        self.assertEqual(receipt_type.type, 'Type')
        self.assertEqual(receipt_type.name, 'Name')
        self.assertEqual(receipt_type.description, 'Description')

    def test_save(self):
        receipt_type = self.__new_receipt_type()
        receipt_type_save = service.save(receipt_type)
        self.check_data(receipt_type_save)

    def test_find(self):
        receipt_type = self.__new_receipt_type()
        receipt_type_save = service.save(receipt_type)
        self.check_data(receipt_type_save)
        receipt_type_find = service.find(receipt_type_save.id)
        self.assertIsNotNone(receipt_type_find)

    def test_find_all(self):
        receipt_type = self.__new_receipt_type()
        receipt_type1 = self.__new_receipt_type()
        receipt_type1.name = "Name 1"
        receipt_type1.description = "Description 1"
        receipt_type.type = 1
        receipt_type_save = service.save(receipt_type)
        service.save(receipt_type1)
        self.check_data(receipt_type_save)
        receipt_types = service.find_all()
        self.assertIsNotNone(receipt_types)
        self.assertEqual(len(receipt_types), 2)

    def test_find_by(self):
        receipt_type = self.__new_receipt_type()
        receipt_type_save = service.save(receipt_type)
        self.check_data(receipt_type_save)
        receipt_type_find_by = service.find_by(type = 1)
        self.assertIsNotNone(receipt_type_find_by)

    def test_update(self):
        receipt_type = self.__new_receipt_type()
        receipt_type_save = service.save(receipt_type)
        receipt_type_save.type = 0
        receipt_type_update_save = service.save(receipt_type_save)
        self.assertEqual(receipt_type_update_save.type, 0)
        self.assertEqual(receipt_type_update_save.name, receipt_type_save.name)
        self.assertEqual(receipt_type_update_save.description, receipt_type_save.description)

    def test_delete(self):
        receipt_type = self.__new_receipt_type()
        receipt_type_save = service.save(receipt_type)
        self.check_data(receipt_type_save)
        receipt_type_delete = service.delete(receipt_type_save)
        self.assertIsNone(receipt_type_delete)

    def __new_receipt_type(self):
        receipt_type = ReceiptType()
        receipt_type.type = 1
        receipt_type.name = "Name"
        receipt_type.description = "Description"
        return receipt_type
    
    def check_data(self, receipt_type_save):
        self.assertIsNotNone(receipt_type_save)
        self.assertIsNotNone(receipt_type_save.id)
        self.assertGreater(receipt_type_save.id, 0)
