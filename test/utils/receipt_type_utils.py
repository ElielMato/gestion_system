from app.models import ReceiptType

def new_receipt_type(id, name, description, entry):
    receipt_type = ReceiptType()
    receipt_type.id = id
    receipt_type.name = name
    receipt_type.description = description
    receipt_type.entry = entry
    return receipt_type