from app.models import Receipt, ReceiptType

def new_receipt(id_header: int, id_footer: int, receipt_type: ReceiptType) -> Receipt:
    receipt = Receipt()
    receipt.id_header = id_header
    receipt.id_footer = id_footer
    receipt.receipt_type = receipt_type
    return receipt