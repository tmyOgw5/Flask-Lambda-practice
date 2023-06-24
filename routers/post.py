from flask import Blueprint, request
from flask_restx import Api, Resource, Namespace, fields
from werkzeug.datastructures import FileStorage
#from database.database import db, UserPost

# Blueprintの作成
app = Blueprint('post', __name__)
api = Api(app)

# パーサーとモデルの定義
upload_parser = api.parser()
upload_parser.add_argument('file', location='files',
                           type=FileStorage, required=True)

resource_fields = api.model("Json Body", {
    "username": fields.String,
    "title": fields.String,
    "content": fields.String,
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
    

@ns.route('/userpost/')
class UserPost(Resource):
    @ns.expect(resource_fields)
    def post(self):
        
        return {'body': "body"}

# NamespaceをBlueprintに追加
api.add_namespace(ns)

