# -*- coding: utf-8 -*-
import os, sys, codecs, io
from flask import Flask, request, render_template, Markup ,redirect ,jsonify
import shutil
import boto3

import db


# 文字コードエラーへの対応
sys.stdout = codecs.getwriter("utf-8")(sys.stdout)
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

app = Flask(__name__)

db.make_db()

@app.route('/')
def top_page():
    return render_template('index.html')


@app.route('/new.html')
def new_page():
    return render_template('new.html')


@app.route('/show.html')
def show_page():
    name = request.args.get('name')
    result = db.link_show(name)
    return render_template('show.html', result=Markup(result), name=name)

@app.route('/new_link.html')
def new_link():
    name = request.args.get('name')
    return render_template('new_link.html', name=name)

@app.route('/new_file.html')
def new_file():
    name = request.args.get('name')
    return render_template('new_file.html', name=name)

@app.route('/file_add.html', methods=["POST"])
def create_file():
    title = request.form["title"]
    uploaded_file = request.files['file']
    description = request.form["description"]

    # 参考:https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.put_object
    s3 = boto3.client('s3', region_name = 'ap-northeast-1')
    # ・title.encode().decode()の所について
    # そのままtitleですると、AWS S3にアップした際に、空白になった
    # titleの部分のstringがutf-8にデコードされてない？
    # しかし、本来Python3では元からデコードされるそうです…。
    # 結論：とりあえずこれで動いたので放置
    s3.put_object(
        Body = io.BufferedReader(uploaded_file).read(),
        Bucket = 'carrierwaveapp2',
        Key = f'{title.encode().decode()}/{uploaded_file.filename}'
    )

    # Todo:アップをミスした場合の処理

    db.add_file(title, uploaded_file.filename, description)

    return redirect('show.html?name='+title)

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
    
    add_result = db.add_group(title, author, description)

    if add_result:
        return redirect('main.html')
    
    else:
        result = db.show_db()
        same_exist=""" 
        <div class="text-center h4 my-4 text-danger">既に同じタイトルのまとめが存在します。</div>
        """
        return render_template('main.html', result=Markup(result) , same_exist=Markup(same_exist))


    

if __name__ == "__main__":
    app.run(debug=True)