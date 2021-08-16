from app import create_app, db
from flask_script import Manager, Server

app = create_app('production')
