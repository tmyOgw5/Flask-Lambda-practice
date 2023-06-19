from flask import Flask, Blueprint
from flask_restx import Api
from routers import get, post

app = Flask(__name__)
# Blueprintの作成
api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_namespace(get.ns)
api.add_namespace(post.ns)

# getモジュールでJson Bodyモデルを登録
api.models[get.resource_fields.name] = get.resource_fields

# postモジュールでJson Bodyモデルを登録
api.models[post.resource_fields.name] = post.resource_fields

app.register_blueprint(api_bp, url_prefix='/api/')


if __name__ == '__main__':
    app.run(debug=True)

"""
@api.route('/', methods=['GET', 'POST'])
def lambda_handler(event=None, context=None):
    
    return 'hello!'
"""