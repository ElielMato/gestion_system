from app.models import Receipt

def new_receipt(id, receipt_type_id, header_id, footer_id):
    receipt = Receipt()
    receipt.id = id
    receipt.receipt_type_id = receipt_type_id
    receipt.header_id = header_id
    receipt.footer_id = footer_id
    return receipt