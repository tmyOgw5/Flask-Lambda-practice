from flask import Flask, Blueprint
from flask_restx import Api
from routers import get, post
from flask import Flask
from database import models
from database.database import engine
from database.database import get_db




app = Flask(__name__)

# Blueprintの作成
api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_namespace(get.ns)
api.add_namespace(post.ns)

# getモジュールでJson Bodyモデルを登録
api.models[get.resource_fields.name] = get.resource_fields

# postモジュールでJson Bodyモデルを登録
api.models[post.resource_fields.name] = post.resource_fields

api.models[post.post_base_model.name] = post.post_base_model
api.models[post.post_display_model.name] = post.post_display_model

app.register_blueprint(api_bp, url_prefix='/api/')

models.Base.metadata.create_all(engine)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db = get_db()
    db.close()

if __name__ == '__main__':
    app.run(debug=True)

"""
@api.route('/', methods=['GET', 'POST'])
def lambda_handler(event=None, context=None):
    
    return 'hello!'
"""