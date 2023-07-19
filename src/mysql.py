import pymysql
 
# データベースに接続
connection = pymysql.connect(host='mysql',
                             user='audel',
                             password='audel_pass',
                             database='audel_db',
                             cursorclass=pymysql.cursors.DictCursor)
 

def data_insert():
    with connection:
        with connection.cursor() as cursor:
            sql = "INSERT INTO "

with connection:
    with connection.cursor() as cursor:
        # レコードを挿入
        sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        cursor.execute(sql, ('webmaster@python.org', 'very-secret'))
 
    # コミットしてトランザクション実行
    connection.commit()