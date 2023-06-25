from flask import Blueprint, request
from flask_restx import Api, Resource, Namespace, fields
from werkzeug.datastructures import FileStorage
from sqlalchemy.orm.session import Session
from database import db_post
from database.database import get_db




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
post_base_model = api.model('PostBase', {
    'image_url': fields.String(required=True),
    'title': fields.String(required=True),
    'content': fields.String(required=True),
    'creator': fields.String(required=True),
})

post_display_model = api.model('PostDisplay', {
    'id': fields.Integer(readOnly=True),
    'image_url': fields.String(required=True),
    'title': fields.String(required=True),
    'content': fields.String(required=True),
    'creator': fields.String(required=True),
    'timestamp': fields.DateTime(dt_format='rfc822'),
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
    @api.expect(post_base_model)
    @api.marshal_with(post_display_model)
    def post(self):
        db = get_db()  # Replace this with your actual db session getter
        data = request.json
        post = db_post.create_post(db, data)  # Replace this with your actual create method
        return post

# NamespaceをBlueprintに追加
api.add_namespace(ns)

