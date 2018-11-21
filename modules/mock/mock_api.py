#-*- coding= utf-8 -*-
from flask import render_template
from . import mock_api
@mock_api.route('/')
def index():
    return render_template('base.html')
@mock_api.route('/search/')
def search():
    return render_template('base.html')