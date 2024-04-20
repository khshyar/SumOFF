import mysql.connector

class SqlPy():
    def __init__(self):
        self.conn = mysql.connector.connect(
            host='localhost', username='root', password='SumOFF180424!', database='sumoff')



    def push_db(self, email,username_data,password_data):
        my_cursor = self.conn.cursor()

        my_cursor.execute(
            "INSERT INTO user (`email`, `username`, `password`) VALUES (%s, %s, %s)",
            (email, username_data, password_data)
        )

        self.conn.commit()
        self.conn.close()

        print("Connection successfully created")
