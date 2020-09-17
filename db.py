import sqlite3
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

    con.commit()
    cur.close()
    con.close()


# groupの追加
def add_group(title, author, description, password):
    con = sqlite3.connect('title.db')
    cur = con.cursor()

    sql = 'insert into groups_db (title, author, description, password) values (?,?,?,?)'
    cur.execute(sql, (title, author, description, password))
    con.commit()

    cur.close()
    con.close()

def add_link(title, link_title, url, description):
    con = sqlite3.connect('title.db')
    cur = con.cursor()

    sql = 'insert into links_db (title, link_title, url, description) values (?,?,?,?)'
    cur.execute(sql, (title, link_title, url, description))
    con.commit()

    cur.close()
    con.close()


def show_db():
    result = ""
    content = []
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
    content = []
    con = sqlite3.connect('title.db')
    cur = con.cursor()
    con.text_factory = str

    sql = 'select * from links_db where title="'+ name +'"'
    group_sql = 'select * from groups_db where title="'+ name +'"'

    group_text = """
    <h2 class="py-3">{title}</h2>
    <h3>{author}</h3>
    <p>{description}</p>
    <a href="./main.html" class="btn btn-outline-primary mb-3">戻る</a>
    """

    text = """
    <div class="row">
      <div class="col-md-3">
        <h3><a href={url}>{link_title}</a></h3>
      </div>
      <div class="col-md-9">
        <p>{description}</p>
      </div>
    </div>
    """
    
    for row in cur.execute(group_sql):
        result1 += group_text.format(title=row[1], author=row[2] , description=row[3])

    for row in cur.execute(sql):
        result2 += text.format(title=row[1], link_title=row[2], url=row[3], description=row[4], name=row[0])
    cur.close()
    con.close()

    if result2=="":
        result2 = "まだ何も登録してません"

    return result1 + result2