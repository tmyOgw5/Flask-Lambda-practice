from flask import Flask
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app)


@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

    
@api.route('/<name>')
class HelloWorld(Resource):
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