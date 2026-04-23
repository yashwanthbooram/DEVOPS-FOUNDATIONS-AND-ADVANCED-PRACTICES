from flask import Flask
from flask_cors import CORS
from flask_talisman import Talisman

app = Flask(__name__)
Talisman(app)
CORS(app)

from service import routes
