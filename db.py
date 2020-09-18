import sqlite3
import boto3
import hashlib

# ハッシュ値を求める関数
def get_hash(s: str):
    return hashlib.sha256(s.encode()).hexdigest()

# DBの作成
def make_db():
    dbname = 'title.db'
    con = sqlite3.connect(dbname)
    cur = con.cursor()

    create_table = 'create table if not exists groups_db (id integer primary key, title text, author text, description text, password text)'
    cur.execute(create_table)

    create_table = 'create table if not exists links_db (id integer primary key, title text, link_title text, url text, description text)'
    cur.execute(create_table)

    create_table = 'create table if not exists files_db (id integer primary key, title text, file_name text, description text)'
    cur.execute(create_table)

    con.commit()
    cur.close()
    con.close()


# groupの追加
def add_group(title, author, description, password):
    con = sqlite3.connect('title.db')
    cur = con.cursor()

    # 同じグループ名の登録があった場合
    sql = 'select * from groups_db where title="'+ title +'"'
    cur.execute(sql)

    if len(cur.fetchall()):
        print("既に登録されています。",flush=True)
        return False

    sql = 'insert into groups_db (title, author, description, password) values (?,?,?,?)'
    cur.execute(sql, (title, author, description, password))
    con.commit()

    cur.close()
    con.close()
    return True

def add_link(title, link_title, url, description):
    con = sqlite3.connect('title.db')
    cur = con.cursor()

    sql = 'insert into links_db (title, link_title, url, description) values (?,?,?,?)'
    cur.execute(sql, (title, link_title, url, description))
    con.commit()

    cur.close()
    con.close()

def add_file(title, file_name, description):
    con = sqlite3.connect('title.db')
    cur = con.cursor()

    sql = 'insert into files_db (title, file_name, description) values (?,?,?)'
    cur.execute(sql, (title, file_name, description))
    con.commit()

    cur.close()
    con.close()


def show_db():
    result = ""
    con = sqlite3.connect('title.db')
    cur = con.cursor()
    con.text_factory = str

    sql = 'select * from groups_db ORDER BY id DESC'

    text = """
    <div class="card my-3">
      <div class="card-body">
        <h4 class="card-title">{title}</h4>
        <h6 class="card-subtitle">作成者：{author}</h6>
        <p class="card-text">{description}</p>
        <a href="./show.html?name={name}" class="btn btn-outline-primary">まとめを見る</a>
      </div>
    </div>
    """

    for row in cur.execute(sql):
        if row[4]:
            pass
        else:
            result += text.format(title=row[1], author=row[2], description=row[3], name=row[1])

    cur.close()
    con.close()

    return result


# links_dbへの追加
def add_links_db(title, link_title, url, description):
    con = sqlite3.connect('title.db')
    cur = con.cursor()

    sql = 'insert into links_db (title, link_title, url, description) values (?,?,?,?)'
    cur.execute(sql, (title, link_title, url, description))
    con.commit()

    cur.close()
    con.close()


#links_db　表示
def link_show(name):
    result1 = ""
    result2 = ""
    con = sqlite3.connect('title.db')
    cur = con.cursor()
    con.text_factory = str

    sql = 'select * from links_db where title="'+ name +'"'
    group_sql = 'select * from groups_db where title="'+ name +'"'
    file_sql = 'select * from files_db where title="'+ name +'"'

    group_text = """
    <div style="padding:0px 0; margin:20px 0; border-bottom:2px solid grey;">
        <a href="./main.html" class="btn btn-outline-primary mb-3">戻る</a>
        <h2 class="py-3">タイトル：{title}</h2>
        <h5>作成者：{author}</h5>
        <p>説明：{description}</p>
    </div>
    """

    text = """
    <div class="row" style="margin: 20px 0; padding: 20px 0; border-bottom: 2px solid grey;">
      <div class="col-md-4">
        <h3><a href={url}>{link_title}</a></h3>
      </div>
      <div class="col-md-8" style="word-wrap: break-word;">
        <p>{description}</p>
      </div>
    </div>
    """

    file_text = """
    <div class="row">
      <div class="col-md-3">
        <h3><a href="{url}">{file_name}</a></h3>
      </div>
      <div class="col-md-9" style="word-wrap: break-word;">
        <p>{description}</p>
        <div class="text-right">
          <a href="{url}" class="btn btn-outline-primary">ダウンロード</a>
        </div>
      </div>
    </div>
    """
    
    for row in cur.execute(group_sql):
        result1 += group_text.format(title=row[1], author=row[2] , description=row[3])

    for row in cur.execute(sql):
        result2 += text.format(title=row[1], link_title=row[2], url=row[3], description=row[4], name=row[0])

    for row in cur.execute(file_sql):
        title=row[1]
        file_name=row[2]

        s3 = boto3.client('s3', region_name = 'ap-northeast-1')

        url = "test"

        url = s3.generate_presigned_url(
            ClientMethod = 'get_object',
            Params = {'Bucket' : 'carrierwaveapp2', 'Key' : title + '/' + file_name},
            ExpiresIn = 3600,
            HttpMethod = 'GET'
        )

        result1 += file_text.format(url = url, file_name=file_name, description=row[2])

    cur.close()
    con.close()

    if result2=="":
        result2 = """
        <h3>まだ何も登録してません</h3><br>
        """

    return result1 + result2