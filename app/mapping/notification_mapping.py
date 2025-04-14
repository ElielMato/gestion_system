from marshmallow import fields, Schema, post_load
from app.models import Notification

class NotificationMap(Schema):
    id = fields.Integer(dump_only=True)
    type = fields.String(required=True)
    message = fields.String(required=True)
    date = fields.DateTime(dump_only=True)
    
    @post_load
    def make_notification(self, data, **kwargs):
        return Notification(**data)