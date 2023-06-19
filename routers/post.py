from flask import Blueprint, request
from flask_restx import Api, Resource, Namespace, fields
from werkzeug.datastructures import FileStorage

# Blueprintの作成
app = Blueprint('post', __name__)
api = Api(app)

# パーサーとモデルの定義
upload_parser = api.parser()
upload_parser.add_argument('file', location='files',
                           type=FileStorage, required=True)

resource_fields = api.model("Json Body", {
    "key1": fields.String,
    "key2": fields.Integer,
    "key3": fields.Boolean,
})

# Namespaceの作成
ns = Namespace('post', description='Post operations')

@ns.route('/file/')
@ns.expect(upload_parser)
class FileUpload(Resource):
    def post(self):
        args = upload_parser.parse_args()
        uploaded_file = args['file']  # This is FileStorage instance
        return {'image': 'image', 'message': 'success', 'file': uploaded_file.filename}

# NamespaceをBlueprintに追加
api.add_namespace(ns)

