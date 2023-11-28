from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

db = SQLAlchemy(app)

@app.route('/')
def index():
    return 'Hello!. Please signup, if not sign-in '


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')