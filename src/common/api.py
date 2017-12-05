import flask_restful

from .representations.json import output_json


class Api(flask_restful.Api):
    def __init__(self, *args, **kwargs):
        super(Api, self).__init__(*args, **kwargs)
        self.representations.update({
            'application/json': output_json,
        })
