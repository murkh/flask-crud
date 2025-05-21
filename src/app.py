import os
from flask import Flask
from . import create_app
from .accounts.urls import accounts_bp
from .books.urls import books_bp
from .authors.urls import authors_bp

app = create_app(os.getenv("CONFIG_MODE", "development"))

# Register blueprints
app.register_blueprint(accounts_bp)
app.register_blueprint(books_bp)
app.register_blueprint(authors_bp)


@app.route("/")
def hello():
    return "HELLO WORLD"


if __name__ == "__main__":
    app.run()
