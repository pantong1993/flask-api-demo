#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Author  : pantong
# @Time    : 2020/1/8 19:35
# @File    : api.py
# @Function:
from flask_restful import Resource


class Hello(Resource):
    def get(self):
        return {"hello": "world"}
