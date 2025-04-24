from dataclasses import dataclass
from app import db

@dataclass(init=True, eq=True)
class Receipt(db.Model):
    """
    Modelo para representar un recibo completo
    """
    __tablename__ = 'receipts'
    id: int = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    receipt_type_id: int = db.Column('receipt_type_id', db.Integer, db.ForeignKey('receipt_types.id'), nullable=False)
    header_id: int = db.Column('receipt_header_id', db.Integer, db.ForeignKey('receipt_headers.id'), nullable=False)
    footer_id: int = db.Column('receipt_footer_id', db.Integer, db.ForeignKey('receipt_footers.id'), nullable=False)
    items = db.relationship('ReceiptItem', back_populates='receipt')