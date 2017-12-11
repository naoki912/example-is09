from model_schema import ma
from model.settlement import Settlement


class SettlementSchema(ma.ModelSchema):
    class Meta:
        model = Settlement
