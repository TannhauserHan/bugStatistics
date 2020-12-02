import pymysql
from BugSql import *
def connect_db(sql):
    connection = pymysql.connect(
    host='localhost',
    user ='root',
    password = 'root',
    db = 'zentao',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
    )
    try:
        with connection.cursor() as target:
            target.execute(sql)
            res = target.fetchall()
#            for res in result:
#                print(res)
    finally:
        connection.close()
    return res
