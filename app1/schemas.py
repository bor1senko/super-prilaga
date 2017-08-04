from marshmallow_sqlalchemy import ModelSchema
from models import Spiner

class SpienrSchema(ModelSchema):
    class Meta:
        model = Spiner

