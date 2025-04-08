from app import db
from app.models import Receipt
from app.repositories import CreateAbstractRepositories, ReadAbstractRepositories, DeleteAbstractRepositories

class ReceiptRepositories(CreateAbstractRepositories, ReadAbstractRepositories, DeleteAbstractRepositories):
    def save(self, receipt: Receipt) -> Receipt:
        db.session.add(receipt)
        db.session.commit()
        return receipt

    def find(self, receipt_id: int) -> Receipt:
        return Receipt.query.get(receipt_id)

    def find_all(self) -> list:
        return Receipt.query.all()

    def delete(self, receipt: Receipt) -> None:
        db.session.delete(receipt)
        db.session.commit()

    def find_by(self, **kwargs) -> Receipt:
        return Receipt.query.filter_by(**kwargs).first()