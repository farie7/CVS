# from models import User
import os
from flask import Flask
from flask_mail import Mail, Message
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    uploads_dir = os.path.join(app.instance_path, 'verified_students')
    # Create a directory in a known location to save files to.
    os.makedirs(uploads_dir, exist_ok=True)
    # # email configuration
    #
    # # configuration of mail
    # app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    # app.config['MAIL_PORT'] = 465
    # app.config['MAIL_USERNAME'] = 'yourId@gmail.com'
    # app.config['MAIL_PASSWORD'] = '*****'
    # app.config['MAIL_USE_TLS'] = False
    # app.config['MAIL_USE_SSL'] = True

    app.config['STUDENTS_FOLDER'] = uploads_dir
    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECURITY_PASSWORD_SALT']="9hssaoik228a;kslkawii83wepmdswq"
    # mail = Mail(app)
    db.init_app(app)
    migrate.init_app(app, db)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # blueprint for auth routes in our app
    from auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
