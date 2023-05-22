import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

basedir = os.path.abspath(os.path.dirname(__file__))

# init extensions
db = SQLAlchemy()
login_manager = LoginManager()
# login_manager.login_view = "auth.login"
login_manager.login_message_category = "info"


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "my_secret_key"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{os.path.join(basedir, 'data.sqlite')}"

    # init extensions
    login_manager.init_app(app)
    db.init_app(app)

    # register blueprints
    from .controllers import blueprints
    for bp in blueprints():
        app.register_blueprint(bp, url_prefix=f"/{bp.name}")

    from .controllers.index import bp
    app.register_blueprint(bp, url_prefix=f"/")

    return app


app = create_app()
