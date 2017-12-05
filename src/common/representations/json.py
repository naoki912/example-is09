from flask import current_app
from flask import make_response
from flask.json import dumps


def output_json(data, code, headers=None):
    """
    Flask responseで使用するJSON encoded bodyを作成する

    flask_restfulのoutput_jsonは、公式のjsonモジュールを使用しているが、
    datetime型をうまくシリアライズ出来ないので、flask.jsonを使用するようにしたもの
    """

    settings = current_app.config.get('RESTFUL_JSON', {})

    dumped = dumps(data, **settings) + "\n"

    resp = make_response(dumped, code)
    resp.headers.extend(headers or {})
    return resp
