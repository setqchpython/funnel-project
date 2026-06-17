from flask import Flask

def create_app():
    app = Flask(__name__)
    
    from app.routes.ask import ask_bp
    from app.routes.web import web_bp

    app.register_blueprint(ask_bp)
    app.register_blueprint(web_bp)
    
    return app