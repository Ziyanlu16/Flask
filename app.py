from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configure MySQL connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '19981128qwER@'
app.config['MYSQL_DB'] = 'mydatabase'

mysql = MySQL(app)

with app.app_context():
    cursor = mysql.connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS example (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))''')
    mysql.connection.commit()
    cursor.close()