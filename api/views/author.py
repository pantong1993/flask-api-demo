#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Author  : pantong
# @Time    : 2020/1/9 10:09
# @File    : author.py
# @Function: 作者

from flask import request
from flask_restful import Resource, fields, marshal_with, reqparse

from api import db
from api.models import Author


def author_ser(author):
    return {
        "id": author.id,
        "name": author.name
    }


author_field = {
    "code": fields.String,
    "msg": fields.String,
    "data": fields.Nested({
        "id": fields.Integer,
        "name": fields.String
    })
}


class AuthorView(Resource):

    @marshal_with(fields=author_field)
    def get(self):
        authors = Author.query.all()
        return {"code": 1000, "msg": "ok", "data": authors}

    def post(self):
        name = request.json.get("name")
        author = Author(name=name)
        db.session.add(author)
        db.session.commit()
        return {"code": 1000, "msg": "ok", "data": author_ser(author)}


class AuthorOneView(Resource):

    @marshal_with(fields=author_field)
    def get(self, id):
        print(id)
        author = Author.query.filter(Author.id == id).first()
        return {"code": 1000, "msg": "ok", "data": author}

    def put(self, id):
        name = request.json.get("name")
        print(name)
        Author.query.filter(Author.id == id).update({"name": name})
        db.session.commit()

        return {"code": 1000, "msg": "ok"}

    def delete(self, id):
        try:
            Author.query.filter(Author.id == id).delete(synchronize_session=False)
            db.session.commit()
            return {"code": 1000, "msg": "ok"}
        except:
            db.session.rollback()
            return {"code": 1001, "msg": "删除失败"}
