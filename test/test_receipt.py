# from datetime import datetime
# import os
# import unittest
# from app import create_app
# from app import db
# from app.models import Receipt, ReceiptType, ReceiptHeader, ReceiptItem, ReceiptFooter
# from app.services import ReceiptService
# service = ReceiptService()

# class ReceiptTestCase(unittest.TestCase):
#     """
#     Test Receipt Model
#     We apply principle such as DRY, KISS, YAGNI and, SOLID
#     """

#     def setUp(self):
#         os.environ['FLASK_CONTEXT'] = 'testing'
#         self.app = create_app()
#         self.app_context = self.app.app_context()
#         self.app_context.push()
#         db.create_all()

#     def tearDown(self):
#         db.session.remove()
#         db.drop_all()
#         self.app_context.pop()

#     def test_receipt(self):
#         receipt = self.__new_receipt()
#         self.assertEqual(receipt.header.id, 1)
#         self.assertEqual(receipt.footer.id, 1)
#         self.assertEqual(len(receipt.items), 3)

#     def test_save(self):
#         receipt = self.__new_receipt()
#         receipt_save = service.save(receipt)
#         self.check_data(receipt_save)

#     def test_find(self):
#         receipt = self.__new_receipt()
#         receipt_save = service.save(receipt)
#         self.check_data(receipt_save)
#         receipt_find = service.find(receipt_save.id)
#         self.assertIsNotNone(receipt_find)

#     def test_find_all(self):
#         receipt = self.__new_receipt()
#         receipt1 = self.__new_receipt()

#     def test_find_by(self):
#         receipt = self.__new_receipt()
#         receipt_save = service.save(receipt)
#         self.check_data(receipt_save)
#         receipt_find_by = service.find_by(id = 1)
#         self.assertIsNotNone(receipt_find_by)

#     def test_update(self):
#         receipt = self.__new_receipt()
#         receipt_save = service.save(receipt)

#     def test_delete(self):
#         receipt = self.__new_receipt()
#         receipt_save = service.save(receipt)
#         self.check_data(receipt_save)
#         receipt_delete = service.delete(receipt_save)
#         self.assertIsNone(receipt_delete)
    
#     def __get_receipt_header(self) -> ReceiptHeader:
#         header = ReceiptHeader()
#         header.submission_date = datetime.now()
#         return header

#     def __get_receipt_item(self) -> list[ReceiptItem]:
#         items = []
#         items.append(ReceiptItem(id_article=1, quantity=10, batch='batch1'))
#         items.append(ReceiptItem(id_article=2, quantity=5, batch='batch2'))
#         items.append(ReceiptItem(id_article=3, quantity=2, batch='batch3'))
#         return items

#     def __get_receipt_footer(self) -> ReceiptFooter:
#         footer = ReceiptFooter()
#         footer.total = 100.0
#         return footer
    
#     def __new_receipt(self) -> Receipt:
#         header = self.__get_receipt_header()
#         items = self.__get_receipt_item()
#         footer = self.__get_receipt_footer()
#         receipt = Receipt()
#         receipt.header = header
#         receipt.items = items
#         receipt.footer = footer
#         return receipt
    
#     def check_data(self, save):
#         self.assertIsNotNone(save)
#         self.assertIsNotNone(save.id)
#         self.assertGreater(save.id, 0)

# if __name__ == '__main__':
#     unittest.main()

from datetime import datetime
import os
import unittest
from app import create_app
from app import db
from app.models import Receipt, ReceiptFooter, ReceiptHeader, ReceiptItem, ReceiptType
from app.services import ReceiptService




class ReceiptTestCase(unittest.TestCase):
    """
    Receipt Mode
    Necesitamos aplicar principios como DRY( Don't repeat yourself) y KISS (Keep it Simple, Stupid).
    YAGNI (You aren't gonna need it) y SOLID (Single responsability principle).
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
    
    def test_receipt_creation(self):
        receipt = Receipt()
        
        header = self.__get_header()
        items = self.__get_items()
        footer = self.__get_footer()
        receipt.header = header
        receipt.items = items
        receipt.footer = footer
        self.assertEqual(receipt.header.id, header.id)
        self.assertEqual(receipt.footer.id, footer.id)
        self.assertEqual(len(receipt.items), len(items))
    
    def test_receipt_save(self):
        receipt = Receipt()
        
        header = self.__get_header()
        items = self.__get_items()
        footer = self.__get_footer()
        receipt.header = header
        receipt.items = items
        receipt.footer = footer
        ReceiptService.save(receipt)
        self.assertIsNotNone(receipt.id)

    def __get_header(self) -> ReceiptHeader:
        header = ReceiptHeader() 
        header.id = 1
        header.submission_date = datetime.now()
        return header


    def __get_items(self) -> list[ReceiptItem]:
        items = []
        items.append(ReceiptItem(id=1, id_article=1, quantity=2.0, batch='batch1')) 
        items.append(ReceiptItem(id=2, id_article=2, quantity=3.0, batch='batch2'))
        items.append(ReceiptItem(id=3, id_article=3, quantity=4.0, batch='batch3'))
        return items
    
    def __get_footer(self) -> ReceiptFooter:
        footer = ReceiptFooter()
        footer.id = 1
        footer.total = 100.0
        return footer
    