# the manage.py file is necessary in order to update heroku
# whenever we add a migration to our app. This keeps heroku
#updated with all of our local changes automatically.
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app
from models import db

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
