# -*- coding: utf-8 -*-
"""
@time           : 2021/9/6 下午12:15
@author         : liuning@shanshu.ai
@file           : app.py
@description    : CODF dispatch Engine Application Web Server Main
"""
import os
from flask_restful import Resource
from flask import make_response
from flask import Flask
from flask_restful import Api


class IndexApi(Resource):
    """Index Root.

    """

    def get(self):
        response = make_response('Docker Flask Web')
        response.status_code = 200
        response.headers['content-type'] = 'application/json'
        return response


app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
api = Api(app)

api.add_resource(IndexApi, '/api')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8888)
