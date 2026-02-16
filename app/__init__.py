from flask_mail import Mail, Message
from flask_cors import CORS
from flask import Flask
from dotenv import load_dotenv
from app.config import Config

mail = Mail()

def create_app():
    load_dotenv()

    app = Flask(__name__)
    
    app.config.from_object(Config)
    
    mail.init_app(app)
    CORS(app)
    
    from app.routes.auth_routes import auth_bp
    from app.routes.main_routes import main_bp
    from app.routes.user_routes import user_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(user_bp)

    return app