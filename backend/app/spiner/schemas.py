from marshmallow_sqlalchemy import ModelSchema
from models import Spiner


class SpinerSchema(ModelSchema):
    class Meta:
        model = Spiner
