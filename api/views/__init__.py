#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask_restful import Api
from .api import Hello
from .author import AuthorView, AuthorOneView
from .publisher import PublisherView, PublisherOneView
from .book import BookView, BookOneView

api = Api()  # 先在这里创建实例，然后在create_app()中初始化

api.add_resource(Hello, "/hello")
api.add_resource(AuthorView, "/author")
api.add_resource(AuthorOneView, "/author/<int:id>")
api.add_resource(PublisherView, "/publisher")
api.add_resource(PublisherOneView, "/publisher/<int:id>")
api.add_resource(BookView, "/book")
api.add_resource(BookOneView, "/book/<int:id>")
