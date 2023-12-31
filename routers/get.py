from flask import Blueprint, request,render_template,make_response
from flask_restx import Api, Resource, Namespace, fields
from werkzeug.datastructures import FileStorage

# Blueprintの作成
app = Blueprint('practice', __name__)
api = Api(app)

# Namespaceの作成
ns = Namespace('practice', description='get api')

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
    @ns.produces(['text/html'])
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('index.html'),200,headers)
    
@ns.route('/<name>')
class HelloName(Resource):
    @ns.expect(resource_fields)
    def post(self, name):
        body = request.json
        return {'hello': name, 'body': body}

# NamespaceをBlueprintに追加
api.add_namespace(ns)
