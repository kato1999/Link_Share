# -*- coding: utf-8 -*-
import os, sys, codecs, io
from flask import Flask, request, render_template, Markup ,redirect
import shutil

import db


# 文字コードエラーへの対応
sys.stdout = codecs.getwriter("utf-8")(sys.stdout)
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

app = Flask(__name__)

db.make_db()

@app.route('/index.html')
def top_page():
    return render_template('index.html')


@app.route('/new.html')
def new_page():
    return render_template('new.html', content="test")


# @app.route('/show.html')
# def show_page():
    
#     return render_template('show.html', content="test")

@app.route('/show/<id>')
def hello(id=None):
    #return name
    return render_template('show.html', title='flask test', id=id) 

@app.route('/main.html')
def main_page():
    result = db.show_db()

    return render_template('main.html', result=Markup(result))

@app.route('/main_add.html', methods=["POST"])
def main1_page():
    
    title = request.form["title"]
    link = request.form["link"]
    description = request.form["description"]
    
    db.add_db(title, link, description)

    return redirect('main.html')

##コメント

if __name__ == "__main__":
    app.run(debug=True)