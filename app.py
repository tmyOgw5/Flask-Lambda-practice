from flask import Flask,Blueprint
from flask_restx import Api, Resource, Namespace


app = Flask(__name__)
api = Api(app, version='1.0', title='API', description='A simple API')

@api.route('/image')
class ImageConversion(Resource):
    def post(self):
        return {'image': 'image', 'message': 'success'}
    
@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

    
@api.route('/name/<name>')
class HelloName(Resource):
    def get(self, name):
        return {'hello': name}

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