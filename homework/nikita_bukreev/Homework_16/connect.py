import mysql.connector as mysql


def db_query(query):
    db = mysql.connect(
        host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
        port=25060,
        user='st4',
        passwd='AVNS_ANI6HFK07yLk4d9l4Nq',
        database='st4'
    )
    cursor = db.cursor(dictionary=True)
    cursor.execute(query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data
