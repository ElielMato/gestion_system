import os
import unittest
from app import create_app
from app import db
from app.models import ReceiptType
from app.services import ReceiptTypeService

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
        self.assertEqual(receipt_type.entry, 1)
        self.assertEqual(receipt_type.name, 'Name')
        self.assertEqual(receipt_type.description, 'Description')

    def test_save(self):
        receipt_type = self.__new_receipt_type()
        receipt_type_save = ReceiptTypeService.save(receipt_type)
        self.check_data(receipt_type_save)

    def test_find(self):
        receipt_type = self.__new_receipt_type()
        receipt_type_save = ReceiptTypeService.save(receipt_type)
        self.check_data(receipt_type_save)
        receipt_type_find = ReceiptTypeService.find(receipt_type_save.id)
        self.assertIsNotNone(receipt_type_find)

    def test_find_all(self):
        receipt_type = self.__new_receipt_type()
        receipt_type1 = self.__new_receipt_type()
        receipt_type1.name = "Name 1"
        receipt_type1.description = "Description 1"
        receipt_type.entry = 0
        receipt_type_save = ReceiptTypeService.save(receipt_type)
        ReceiptTypeService.save(receipt_type1)
        self.check_data(receipt_type_save)
        receipt_types = ReceiptTypeService.find_all()
        self.assertIsNotNone(receipt_types)
        self.assertEqual(len(receipt_types), 2)

    def test_find_by(self):
        receipt_type = self.__new_receipt_type()
        receipt_type_save = ReceiptTypeService.save(receipt_type)
        self.check_data(receipt_type_save)
        receipt_type_find_by = ReceiptTypeService.find_by(entry = receipt_type.entry)
        self.assertIsNotNone(receipt_type_find_by)

    def __new_receipt_type(self):
        receipt_type = ReceiptType()
        receipt_type.entry = 1
        receipt_type.name = "Name"
        receipt_type.description = "Description"
        return receipt_type
    
    def check_data(self, receipt_type_save):
        self.assertIsNotNone(receipt_type_save)
        self.assertIsNotNone(receipt_type_save.id)
        self.assertGreater(receipt_type_save.id, 0)
