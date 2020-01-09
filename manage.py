from api import create_app
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from api import db

app = create_app()
manager = Manager(app)
Migrate(app, db)
"""
数据库迁移命名
python manage.py db init
python manage.py db migrate # makemirations
python manage.py db upgrade # migrate
"""
manager.add_command("db", MigrateCommand)

if __name__ == '__main__':
    # app.run()
    manager.run()
