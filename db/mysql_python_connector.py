import mysql.connector

class SqlPy:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host='localhost', username='root', password='SumOFF180424!', database='sumoff')



    def push_db(self, email, username_data, password_data):
        
        try:
            my_cursor = self.conn.cursor()

            my_cursor.execute(
                "INSERT INTO user (`email`, `username`, `password`) VALUES (%s, %s, %s)",
                (email, username_data, password_data)
            )

            self.conn.commit()
            print("User inserted successfully")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            # Close cursor
            my_cursor.close()

        print("Connection successfully created")
