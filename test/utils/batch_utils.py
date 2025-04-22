from app.models import Batch

def new_batch(id, code, expiration_date):
    batch = Batch()
    batch.id = id
    batch.code = code
    batch.expiration_date = expiration_date
    return batch
