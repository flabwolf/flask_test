# -*- coding: utf-8 -*-
# !/usr/bin/python
# server.py

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    app.debug = True
    app.run(host='0.0.0.0', port=80)
    return render_template('index.html')
    #return 'Hello'


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=80)