from app.models import ReceiptItem

def new_receipt_items(quantity: int, id_article: int, id_batch: int, id_receipt: int) -> ReceiptItem:
    item = ReceiptItem()
    item.quantity = quantity
    item.id_article = id_article
    item.id_batch = id_batch
    item.id_receipt = id_receipt
    return item