from flask import Flask

# 导入并实例化SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
# 注意：- 必须在导入蓝图之前
#       - 必须导入models.py

from .views import api


def create_app():
    app = Flask(__name__)

    # api初始化, 所有url对应关系在api中定义
    api.init_app(app)

    app.config.from_object("settings.ProConfig")

    # 初始化
    db.init_app(app)

    return app
