from app.models import ReceiptItem

def new_receipt_items(id, quantity, article_id, batch_id, receipt_id):
    item = ReceiptItem()
    item.id = id
    item.quantity = quantity
    item.article_id = article_id
    item.batch_id = batch_id
    item.receipt_id = receipt_id
    return item