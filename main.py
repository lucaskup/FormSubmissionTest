from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
import sys
from io import TextIOWrapper
sys.path.append("..")

import pyproj

app=Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def index():
    paramList = []
    if request.values:
        for key, value in request.values.items():
            paramList.append((key,value))
    return render_template('index.html', parametros = paramList, metodo = request.method)

if __name__=='__main__':
    app.run(debug=True)
