from app.models import ReceiptHeader

def new_receipt_header(id, submission_date):
    header = ReceiptHeader()
    header.id = id
    header.submission_date = submission_date
    return header