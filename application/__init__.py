from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "5hg89y5hv3*#ynf34y14373$#^" 

    from .views import views

    app.register_blueprint(views, url_prefix='/')

    return app
