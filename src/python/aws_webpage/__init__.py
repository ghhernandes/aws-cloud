from flask import Flask

app = Flask(__name__)

from . import comprehend
from . import rekognition

@app.route('/')
def home():
    return 'Home-page'
