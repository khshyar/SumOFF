import mysql.connector

conn = mysql.connector.connect(
    host='localhost', username='root', password='SumOFF180424!', database='sumoff')

my_cursor = conn.cursor()

my_cursor.execute("CREATE TABLE user (userid INTEGER(10))")

# for db in my_cursor:
#     print(db)

# conn.commit()
# conn.close()

print("Connection successfully created")
