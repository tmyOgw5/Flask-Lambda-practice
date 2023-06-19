from flask import Flask,Blueprint, request
from flask_restx import Api, Resource, Namespace, fields
from routers.image import post_image
from werkzeug.datastructures import FileStorage


app = Flask(__name__)


api = Api(app, version='1.0', title='API', description='A simple API',default='practice',default_label='practice')

upload_parser = api.parser()
upload_parser.add_argument('file', location='files',
                           type=FileStorage, required=True)


resource_fields = api.model("Json Body", {
    "key1": fields.String,
    "key2": fields.Integer,
    "key3": fields.Boolean,
})
@api.route('/image/<id>')
@api.expect(upload_parser)
class ImageConversion(Resource):
    def post(self,id):
        args = upload_parser.parse_args()
        uploaded_file = args['file']  # This is FileStorage instance
        return {'image': 'image', 'message': 'success', 'id': id, 'file': uploaded_file.filename}
    
    
    
@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

    
@api.route('/name/<name>')
class HelloName(Resource):
    @api.doc(body=resource_fields)
    def post(self, name):
        body = request.json
        return {
            'hello': name,
            'body': body,}

if __name__ == '__main__':
    app.run(debug=True)

"""
@api.route('/', methods=['GET', 'POST'])
def lambda_handler(event=None, context=None):
    
    return 'hello!'

@api.route('/<name>', methods=['GET', 'POST'])
def hello_name(name):
    
    return 'hello ' + name

if __name__ == '__main__':
    app.run()

"""