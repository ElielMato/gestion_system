from app.models import ReceiptFooter

def new_receipt_footer(id, total):
    footer = ReceiptFooter()
    footer.id = id
    footer.total = total
    return footer