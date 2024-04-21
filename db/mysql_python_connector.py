import mysql.connector

class SqlPy:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host='localhost', username='root', password='SumOFF180424!', database='sumoff')
            self.my_cursor = self.conn.cursor()
        except Error as e:
            print(f"Error connection to MySQL Platform: {e}")


    def user_exists(self,email, username):
        query = "SELECT * FROM user WHERE username = %s OR email = %s"
        self.my_cursor.execute(query, (username,email))
        result = self.my_cursor.fetchone()
        return bool(result)
        


    def push_db(self, email, username_data, password_data):

        try:
            if self.user_exists(email, username_data):
                print("User with this username or email already exists")
                return    

            query = "INSERT INTO user (`email`, `username`, `password`) VALUES (%s, %s, %s)"
            self.my_cursor.execute(query,(email,username_data,password_data))
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
