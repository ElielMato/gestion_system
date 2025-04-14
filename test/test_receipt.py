# from datetime import datetime
# import os
# import unittest
# from app import create_app
# from app import db
# from app.models import Receipt, ReceiptHeader, ReceiptFooter, ReceiptItem
# # from app.services import ReceiptService
# # service = ReceiptService()

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
#         item = self.__get_receipt_item()
#         footer = self.__get_receipt_footer()
#         receipt = Receipt(header=header, items=[item], footer=footer, receipt_type=1)
#         return receipt
    
#     def check_data(self, receipt_save):
#         self.assertIsNotNone(receipt_save)
#         self.assertIsNotNone(receipt_save.id)
#         self.assertGreater(receipt_save.id, 0)

# if __name__ == '__main__':
#     unittest.main()