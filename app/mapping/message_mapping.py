from marshmallow import Schema, fields, validate, post_load

class MessageMap(Schema):

    message:str = fields.String(required=True, dump_only=True)
    code:str = fields.String(required=False, dump_only=True)
    data:dict = fields.Dict(required=False, dump_only=True)