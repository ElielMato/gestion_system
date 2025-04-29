from datetime import datetime
from app.models import Batch

def new_batch(code: str, expiration_date: datetime) -> Batch:
    batch = Batch()
    batch.code = code
    batch.expiration_date = expiration_date
    return batch
