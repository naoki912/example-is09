from model_schema import ma
from model.transition import Transition


class TransitionSchema(ma.ModelSchema):
    class Meta:
        model = Transition
