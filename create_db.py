import mysql.connector 

my = mysql.connector.connect(
    host='localhost',
    user = 'root',
    password = '19981128qwER@'
)

my_cursor = my.cursor()

my_cursor.execute('SHOW DATABASES')

for db in my_cursor:
    print(db)