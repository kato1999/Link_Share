import sqlite3
import boto3

# DBの作成
def make_db():
    dbname = 'title.db'
    con = sqlite3.connect(dbname)
    cur = con.cursor()

    create_table = 'create table if not exists groups_db (title text, author text, description text)'
    cur.execute(create_table)

    create_table = 'create table if not exists links_db (title text, link_title text, url text, description text)'
    cur.execute(create_table)

    create_table = 'create table if not exists files_db (id integer primary key, title text, file_name text, description text)'
    cur.execute(create_table)

    con.commit()
    cur.close()
    con.close()


# groupの追加
def add_group(title, author, description):
    con = sqlite3.connect('title.db')
    cur = con.cursor()

    sql = 'insert into groups_db (title, author, description) values (?,?,?)'
    cur.execute(sql, (title, author, description))
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
    content = []
    con = sqlite3.connect('title.db')
    cur = con.cursor()
    con.text_factory = str

    sql = 'select * from groups_db'

    text = """
    <div class="card my-3">
      <div class="card-body">
        <h4 class="card-title">{title}</h4>
        <h6 class="card-subtitle">{author}</h6>
        <p class="card-text">{description}</p>
        <a href="./show.html?name={name}" class="btn btn-outline-primary">まとめを見る</a>
      </div>
    </div>
    """

    for row in cur.execute(sql):
        result += text.format(title=row[0], author=row[1], description=row[2], name=row[0])
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
    file_sql = 'select * from files_db where title="'+ name +'"'

    group_text = """
    <h2 class="py-3">{title}</h2>
    <h3>{author}</h3>
    <p>{description}</p>
    """

    text = """
    <div class="row">
      <div class="col-md-3">
        <h3><a href={url}>{link}</a></h3>
      </div>
      <div class="col-md-9" style="word-wrap: break-word;">
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
        result1 += group_text.format(title=row[0], author=row[1] , description=row[2])

    for row in cur.execute(sql):
        result2 += text.format(title=row[0], link=row[1], url=row[2], description=row[3], name=row[0])

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
        result2 = "まだ何も登録してません"

    return result1 + result2