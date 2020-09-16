import sqlite3

# DBの作成
def make_db():
    dbname = 'title.db'
    con = sqlite3.connect(dbname)
    cur = con.cursor()

    create_table = 'create table if not exists title_db (id integer primary key ,title text, link text, description text)'

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
        <a href="./show/{id}" class="btn btn-outline-primary">まとめを見る</a>
      </div>
    </div>
    """

    for row in cur.execute(sql):
        result += text.format(id=row[0], title=row[1], link=row[2], description=row[3])
    cur.close()
    con.close()

    return result

def show_table(id):
    result = ""
    content = []
    con = sqlite3.connect('title.db')
    cur = con.cursor()
    con.text_factory = str

    sql = 'select * from title_db where' id
    # 続きは後で