import sqlite3

# 连接到数据库文件（如果不存在则会被创建）
conn = sqlite3.connect('cryptid.db')

# 创建一个游标对象
curs = conn.cursor()

# 在数据库中执行 SQL 命令来创建表
curs.execute("""create table if not exists explorer(
                name text primary key,
                country text,
                description text)""")

curs.execute("""create table if not exists creature(
                name text primary key,
                description text,
                country text,
                area text,
                aka text)""")
conn.commit()

# 关闭连接
conn.close()