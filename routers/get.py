from flask import Blueprint, request
from flask_restx import Api, Resource, Namespace, fields
from werkzeug.datastructures import FileStorage

# Blueprintの作成
app = Blueprint('get', __name__)
api = Api(app)

# Namespaceの作成
ns = Namespace('get', description='get api')

# パーサーとモデルの定義
upload_parser = api.parser()
upload_parser.add_argument('file', location='files',
                           type=FileStorage, required=True)

resource_fields = api.model("Json Body", {
    "name": fields.String,
    "age": fields.Integer,
    "boolean": fields.Boolean,
})

# エンドポイントの定義
@ns.route('/hello/')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

@ns.route('/<name>')
class HelloName(Resource):
    @ns.expect(resource_fields)
    def post(self, name):
        body = request.json
        return {'hello': name, 'body': body}

# NamespaceをBlueprintに追加
api.add_namespace(ns)
