from flask import Flask
from flask_cors import CORS

from routes.news_routes import news_bp
from routes.auth_routes import auth_bp

app = Flask(__name__)

CORS(app)

app.register_blueprint(news_bp)
app.register_blueprint(auth_bp)


@app.route('/')
def home():
    return {
        "message": "NewsSphere AI Backend Running"
    }


if __name__ == '__main__':
    app.run(debug=True)