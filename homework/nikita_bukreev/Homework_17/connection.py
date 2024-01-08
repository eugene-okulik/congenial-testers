import mysql.connector as mysql
import os
import dotenv

dotenv.load_dotenv()


def db_query(query):
    db = mysql.connect(
        user=os.getenv('DB_USER'),
        passwd=os.getenv('DB_PASSW'),
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT'),
        database=os.getenv('DB_NAME')
    )

    cursor = db.cursor(dictionary=True)
    cursor.execute(query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data
