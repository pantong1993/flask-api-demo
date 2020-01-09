#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Author  : pantong
# @Time    : 2020/1/9 10:10
# @File    : publisher.py
# @Function:

from flask import request
from flask_restful import Resource, fields, marshal_with, reqparse

from api import db
from api.models import Publisher


def publisher_ser(publisher):
    return {
        "id": publisher.id,
        "name": publisher.name
    }


class PublisherView(Resource):

    def get(self):
        publishers = Publisher.query.all()
        return {"code": 1000, "msg": "ok", "data": [publisher_ser(publisher) for publisher in publishers]}

    def post(self):
        name = request.json.get("name")
        publisher = Publisher(name=name)
        db.session.add(publisher)
        db.session.commit()
        return {"code": 1000, "msg": "ok", "data": publisher_ser(publisher)}


class PublisherOneView(Resource):

    def get(self, id):
        print(id)
        publisher = Publisher.query.filter(Publisher.id == id).first()
        return {"code": 1000, "msg": "ok", "data": publisher_ser(publisher)}

    def put(self, id):
        name = request.json.get("name")
        print(name)
        publisher = Publisher.query.filter(Publisher.id == id).first()
        publisher.name = name
        db.session.commit()

        return {"code": 1000, "msg": "ok", "data": publisher_ser(publisher)}

    def delete(self, id):
        try:
            Publisher.query.filter(Publisher.id == id).delete()
            db.session.commit()
            return {"code": 1000, "msg": "ok"}
        except Exception as e:
            print(e)
            db.session.rollback()
            return {"code": 1001, "msg": "删除失败"}
