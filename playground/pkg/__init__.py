import os

from flask import Flask
from dotenv import load_dotenv
app = Flask(__name__, static_folder="static")
load_dotenv()
app.secret_key = os.getenv("SECRET_KEY")

from pkg import routes



