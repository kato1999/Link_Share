# -*- coding: utf-8 -*-
import os, sys, codecs, io
from flask import Flask, request, render_template, Markup
import shutil


# 文字コードエラーへの対応
sys.stdout = codecs.getwriter("utf-8")(sys.stdout)
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

app = Flask(__name__)



@app.route('/index.html')
def top_page():
    return render_template('index.html')


@app.route('/new.html')
def new_page():
    return render_template('new.html', content="test")


@app.route('/show.html')
def show_page():
    
    return render_template('show.html', content="test")


@app.route('/main.html')
def main_page():

    return render_template('main.html', text="memo")


if __name__ == "__main__":
    app.run(debug=True)