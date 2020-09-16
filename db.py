import sqlite3

# DBの作成
def make_db():
    dbname = 'title.db'
    con = sqlite3.connect(dbname)
    cur = con.cursor()

    create_table = 'create table if not exists title_db (title text, link text, description text)'

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
        <a href="./show.html" class="btn btn-outline-primary">まとめを見る</a>
      </div>
    </div>
    """

    for row in cur.execute(sql):
        result += text.format(title=row[0], link=row[1], description=row[2])
    cur.close()
    con.close()

    return result

   
