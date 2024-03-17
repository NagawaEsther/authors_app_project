from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from authors_app.extensions import db  
from authors_app.controllers.auth.auth_controller import auth
from authors_app.controllers.auth.books_controller import book
from authors_app.controllers.auth.company_controller import company

def create_app():
    app = Flask(__name__)

    app.config.from_object('config.Config')

    db.init_app(app)
    migrate = Migrate(app, db)  

    # Importing and registering models
    from authors_app.models.user import User
    from authors_app.models.company import Company
    from authors_app.models.books import Book  

    @app.route('/')
    def home():
        return "hello world"


    app.register_blueprint(auth, url_prefix='/api/v1/auth')
    app.register_blueprint(book, url_prefix='/api/v1/book')
    app.register_blueprint(company, url_prefix='/api/v1/company')

    return app

# Debugging: Run the Flask application
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
