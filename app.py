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


@app.route('/show.html')
def show_page():
    name = request.args.get('name')
    result = db.link_show(name)
    return render_template('show.html', result=Markup(result), name=name)

@app.route('/new_link.html')
def new_link():
    name = request.args.get('name')
    return render_template('new_link.html', name=name)

# リンクの追加
@app.route('/show_add.html', methods=["POST"])
def create_link():
    title = request.form["title"]
    link_title = request.form["link_title"]
    url = request.form["url"]
    description = request.form["description"]
    
    db.add_link(title, link_title, url, description)

    return redirect('show.html?name='+title)

@app.route('/main.html')
def main_page():
    result = db.show_db()

    return render_template('main.html', result=Markup(result))

@app.route('/main_add.html', methods=["POST"])
def main1_page():
    
    title = request.form["title"]
    author = request.form["author"]
    description = request.form["description"]
    
    db.add_group(title, author, description)

    return redirect('main.html')


if __name__ == "__main__":
    app.run(debug=True)