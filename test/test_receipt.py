import os
import unittest
from app import create_app
from app import db
from app.models import Receipt, ReceiptHeader, ReceiptFooter
from app.services import ReceiptService
services = ReceiptService()

class ReceiptTestCase(unittest.TestCase):
    """
    Test Receipt model
    Aplicamos principios como DRY, KISS, YAGNI y SOLID.
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

    def test_receipt(self):
        receipt = self.__new_receipt()
        self.assertIsNotNone(receipt)
        self.assertEqual(receipt.id_receipt_header, 1)
        self.assertEqual(receipt.id_receipt_footer, 1)

    def test_save(self):
        receipt = self.__new_receipt()
        receipt_save = services.save(receipt)
        self.check_data(receipt_save)

    def test_find(self):
        receipt = self.__new_receipt()
        receipt_save = services.save(receipt)
        self.check_data(receipt_save)
        receipt_find = services.find(receipt_save.id)
        self.assertIsNotNone(receipt_find)

    def test_find_all(self):
        receipt = self.__new_receipt()
        receipt1 = self.__new_receipt1()
        receipt_save = services.save(receipt)
        services.save(receipt1)
        self.check_data(receipt_save)
        receipts = services.find_all()
        self.assertIsNotNone(receipts)
        self.assertEqual(len(receipts), 2)

    def test_update(self):
        receipt = self.__new_receipt()
        receipt_save = services.save(receipt)
        receipt_save.id_receipt_footer = 3
        receipt_update = services.save(receipt_save)
        self.assertEqual(receipt_update.id_receipt_footer, 3)
        self.assertEqual(receipt.id_receipt_footer, receipt_update.id_receipt_footer)

    def __new_receipt(self):
        receipt_header = ReceiptHeader(id_receipt_header=1, submission_date="2025-04-08")
        db.session.add(receipt_header)
        db.session.commit()

        receipt_footer = ReceiptFooter(id_receipt_footer=1, total=100.0)
        db.session.add(receipt_footer)
        db.session.commit()

        receipt = Receipt(id_receipt_header=1, id_receipt_footer=1)
        return receipt
    
    def __new_receipt1(self):
        receipt_header = ReceiptHeader(id_receipt_header=2, submission_date="2025-04-08")
        db.session.add(receipt_header)
        db.session.commit()

        receipt_footer = ReceiptFooter(id_receipt_footer=2, total=100.0)
        db.session.add(receipt_footer)
        db.session.commit()

        receipt = Receipt(id=2, id_receipt_header=2, id_receipt_footer=2)
        return receipt

    def check_data(self, receipt_save):
        self.assertIsNotNone(receipt_save)
        self.assertIsNotNone(receipt_save.id)
        self.assertGreater(receipt_save.id, 0)


if __name__ == '__main__':
    unittest.main()