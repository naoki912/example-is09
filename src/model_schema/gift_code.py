from model_schema import ma
from model.gift_code import GiftCode


class GiftCodeSchema(ma.ModelSchema):
    class Meta:
        model = GiftCode
