from app import create_app, db
from flask_script import Manager, Server

app = create_app('production')
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('server', Server)
manager.add_command('db', MigrateCommand)
