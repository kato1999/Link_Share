import sqlite3

# DBの作成
def make_db():
    dbname = 'title.db'
    con = sqlite3.connect(dbname)
    cur = con.cursor()

    create_table = 'create table if not exists title_db (title text, link text, description text)'
    cur.execute(create_table)

    create_table = 'create table if not exists page_db (title text, link text, url text, description text)'
    cur.execute(create_table)

    con.commit()
    cur.close()
    con.close()


# DBへの追加
def add_db(title, link, description):
    con = sqlite3.connect('title.db')
    cur = con.cursor()

    sql = 'insert into title_db (title, link, description) values (?,?,?)'
    cur.execute(sql, (title, link, description))
    con.commit()

    cur.close()
    con.close()


def show_db():
    result = ""
    content = []
    con = sqlite3.connect('title.db')
    cur = con.cursor()
    con.text_factory = str

    sql = 'select * from title_db'

    text = """
    <div class="card my-3">
      <div class="card-body">
        <h4 class="card-title">{title}</h4>
        <h6 class="card-subtitle">{link}</h6>
        <p class="card-text">{description}</p>
        <a href="./show.html?name={name}" class="btn btn-outline-primary">まとめを見る</a>
      </div>
    </div>
    """

    for row in cur.execute(sql):
        result += text.format(title=row[0], link=row[1], description=row[2], name=row[0])
    cur.close()
    con.close()

    return result


# page_dbへの追加
def add_page_db(title, link, url, description):
    con = sqlite3.connect('title.db')
    cur = con.cursor()

    sql = 'insert into page_db (title, link, url, description) values (?,?,?,?)'
    cur.execute(sql, (title, link, url, description))
    con.commit()

    cur.close()
    con.close()


#page_db　表示
def show2_db():
    result = ""
    content = []
    con = sqlite3.connect('title.db')
    cur = con.cursor()
    con.text_factory = str

    sql = 'select * from page_db'

    text = """
    <h2 class="py-3">{title}</h2>
    
    <div class="row">
      <div class="col-md-3">
        <h3><a href={url}>{link}</a></h3>
      </div>
      <div class="col-md-9">
        <p>{description}</p>
      </div>
    </div>
    
    <div class="row">
      <div class="col-md-3">
        <h3><a href="{url}">{link}</a></h3>
      </div>
      <div class="col-md-9">
        <p>{description}</p>
      </div>
    </div>
    """

    for row in cur.execute(sql):
        result += text.format(title=row[0], link=row[1], url=row[2], description=row[3], name=row[0])
    cur.close()
    con.close()

    return result