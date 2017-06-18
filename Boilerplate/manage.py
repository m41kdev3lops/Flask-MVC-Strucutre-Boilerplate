# -*- coding: utf-8 -*-
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from src.app import app, db


migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

from src.models import mainModel

if __name__ == '__main__':
    manager.run()