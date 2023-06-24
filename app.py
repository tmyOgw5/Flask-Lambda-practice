from flask import Flask, Blueprint
from flask_restx import Api
from routers import get, post
from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
#from database.database import db, UserPost
from database import models
from database.database import engine




app = Flask(__name__)
"""
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///api.db"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO']=True
# initialize the app with the extension
db.init_app(app)



with app.app_context():
    db.create_all()

"""








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



models.Base.metadata.create_all(engine)

if __name__ == '__main__':
    app.run(debug=True)

"""
@api.route('/', methods=['GET', 'POST'])
def lambda_handler(event=None, context=None):
    
    return 'hello!'
"""