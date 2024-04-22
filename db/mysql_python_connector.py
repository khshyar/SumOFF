import mysql.connector
from mysql.connector import Error


class SqlPy:
    def __init__(self, host='localhost', username='root', password='SumOFF180424!', database='sumoff'):
        self.conn = None
        self.my_cursor = None
        try:
            self.conn = mysql.connector.connect(host=host, username=username, password=password, database=database)
            self.my_cursor = self.conn.cursor()
        except Error as e:
            print(f"Error connecting to MySQL Platform: {e}")

    
    def user_exists(self, username=None, email=None):
        # Check if username exists
        if username:
            self.my_cursor.execute("SELECT 1 FROM user WHERE username = %s", (username,))
            if self.my_cursor.fetchone():
                return 'username'
        # Check if email exists
        if email:
            self.my_cursor.execute("SELECT 1 FROM user WHERE email = %s", (email,))
            if self.my_cursor.fetchone():
                return 'email'
        return None
    


    def push_db(self, email, username_data, password_data):
        
        try:
            exists = self.user_exists(username=username_data, email=email)
            if exists == 'username':
                print("User with this username already exists")
                return
            elif exists == 'email':
                print("User with this email already exists")
                return
        
            query = "INSERT INTO user (email, username, password) VALUES (%s, %s, %s)"
            self.my_cursor.execute(query, (email, username_data, password_data))
            self.conn.commit()
            print("User inserted successfully") 
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            # Close cursor
            self.my_cursor.close()
            self.my_cursor = self.conn.cursor()
    
    def close_connection(self):
        if self.conn:
            self.conn.close()
            print("Connection closed")

    def __del__(self):
        # Close connection when the object is deleted
        self.close_connection()
