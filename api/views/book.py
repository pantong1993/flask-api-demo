#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Author  : pantong
# @Time    : 2020/1/9 10:09
# @File    : book.py
# @Function:

from flask import request
from flask_restful import Resource, fields, marshal_with, reqparse

from api import db
from api.models import Book, Author

from .author import author_ser
from .publisher import publisher_ser


def book_ser(book):
    return {
        "id": book.id,
        "title": book.title,
        "publisher_name": publisher_ser(book.publisher),
        "author": [author_ser(i) for i in book.authors]
    }


book_field = {
    "code": fields.String,
    "msg": fields.String,
    "data": fields.Nested({
        "id": fields.Integer,
        "title": fields.String,
        "publisher": fields.Nested({
            "id": fields.Integer,
            "name": fields.String
        }),
        "authors": fields.List(fields.Nested({
            "id": fields.Integer,
            "name": fields.String
        }))
    })
}


class BookView(Resource):

    @marshal_with(fields=book_field)
    def get(self):
        books = Book.query.all()
        return {"code": 1000, "msg": "ok", "data": books}

    def post(self):
        title = request.json.get("title")
        publisher_id = request.json.get("publisher_id")
        author_list = request.json.get("author_list")
        aut_list = []
        for i in author_list:
            aut_list.append(Author.query.filter(Author.id == i).first())

        book = Book(title=title, publisher_id=publisher_id, authors=aut_list)
        db.session.add(book)
        db.session.commit()
        return {"code": 1000, "msg": "ok", "data": book_ser(book)}


class BookOneView(Resource):

    @marshal_with(fields=book_field)
    def get(self, id):
        print(id)
        book = Book.query.filter(Book.id == id).first()
        return {"code": 1000, "msg": "ok", "data": book}

    def put(self, id):
        title = request.json.get("title")
        publisher_id = request.json.get("publisher_id")
        author_list = request.json.get("author_list")
        aut_list = []
        for i in author_list:
            aut_list.append(Author.query.filter(Author.id == i).first())

        print(aut_list)

        book = Book.query.filter(Book.id == id).first()
        book.title = title
        book.publisher_id = publisher_id
        book.authors = aut_list
        db.session.commit()

        return {"code": 1000, "msg": "ok", "data": book_ser(book)}

    def delete(self, id):
        try:
            Book.query.filter(Book.id == id).delete()
            db.session.commit()
            return {"code": 1000, "msg": "ok"}
        except:
            db.session.rollback()
            return {"code": 1001, "msg": "删除失败"}
