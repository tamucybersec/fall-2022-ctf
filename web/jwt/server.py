#!/usr/bin/env python3

import jwt
from flask import Flask, render_template_string, request, Response

app = Flask(__name__)

secret = 'coconutmall'
flag = open('flag.txt').read()

@app.route('/')
def index():
    return Response(open(__file__).read(), mimetype='text/plain')

@app.route('/api/register', methods=['POST'])
def register():
    if 'username' in request.form:
        username = request.form['username']
        return {'session': jwt.encode({'username':username, 'admin':False}, secret, algorithm='HS256')}
    else:
        return {"err": "username expected"}

@app.route('/api/login', methods=['POST'])
def login():
    if 'session' in request.form:
        decoded = jwt.decode(request.form['session'], secret, algorithms=['HS256'])
        if 'admin' in decoded and decoded['admin'] == True:
            return {"res": f"Here's your flag, admin: {flag}"}
        elif 'username' in decoded:
            return {"res": f"Hello {decoded['username']}, thanks for testing my API!"}
        else:
            return {"err": "problem with session"}
    else:
        return {"err": "token expected"}

app.run('0.0.0.0', 5004)
