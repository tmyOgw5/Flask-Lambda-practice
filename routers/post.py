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
    'image_url': fields.String(required=True),
    'title': fields.String(required=True),
    'creator': fields.String(required=True),
    'timestamp': fields.DateTime(required=True),
    
})

# Namespaceの作成
ns = Namespace('post', description='Post operations')



@ns.route('/')
class Post(Resource):
    @api.expect(post_base_model)
    @api.marshal_with(post_display_model)
    def post(self):
        db = get_db()  # Replace this with your actual db session getter
        data = request.json
        post = db_post.create_post(db, data)  # Replace this with your actual create method
        return post

@ns.route('/all')
class GetALlPosts(Resource):
    @api.marshal_with(post_display_model)
    def get(self):
        db = get_db()
        posts = db_post.get_all_posts(db)
        return posts

@ns.route('/user/<int:id>')
class GetPostsById(Resource):
    @api.marshal_with(post_display_model)
    def get(self, id):
        db = get_db()
        posts = db_post.get_post_by_id(db, id)
        return posts
    
    def delete(self, id):
        db = get_db()
        posts = db_post.delete_post(db, id)
        return "deleted"


@ns.route('/file/')
@ns.expect(upload_parser)
class FileUpload(Resource):
    def post(self):
        args = upload_parser.parse_args()
        uploaded_file = args['file']  # This is FileStorage instance


        return {'image': 'image', 'message': 'success', 'file': uploaded_file.filename}
    
# NamespaceをBlueprintに追加
api.add_namespace(ns)

