from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
    cnx = mysql.connector.connect(user='root', password='example',
                                   host='db', database='mydatabase')
    cursor = cnx.cursor()
    cursor.execute('SELECT * FROM mytable')
    result = cursor.fetchall()
    return str(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
