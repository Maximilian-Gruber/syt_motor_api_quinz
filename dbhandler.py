import mysql.connector

class DBHandler:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()
        self.cursor.execute("SET sql_mode = ''")
    def insert_data(self, value, type, user):
        query = "INSERT INTO `values` (value, type, user) VALUES (%s, %s, %s)"
        values = (value, type, user)
        self.cursor.execute(query, values)
        self.connection.commit()

    def close_connection(self):
        self.cursor.close()
        self.connection.close()

# Example usage:
# db = DBHandler('localhost', 'your_username', 'your_password', 'your_database')
# db.insert_data(1, 'some_value', 'some_type', 'some_user')
# db.close_connection()