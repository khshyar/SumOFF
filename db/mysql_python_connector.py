import mysql.connector

conn = mysql.connector.connect(
    host='localhost', username='root', password='SumOFF180424!', database='sumoff')

def push_db(email,username_data,password_data):
    my_cursor = conn.cursor()

    my_cursor.execute(
        "INSERT INTO user (`email`, `username`, `password`) VALUES (%s, %s, %s)",
        (email, username_data, password_data)
    )

    conn.commit()
    conn.close()

    print("Connection successfully created")
