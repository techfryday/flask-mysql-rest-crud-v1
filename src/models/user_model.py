
import mysql.connector
import json
class user_model():
    def __init__(self):
        self.db = mysql.connector.connect(host="localhost",user="root",password="",database="test")
        self.cur = self.db.cursor(dictionary=True)
        
    def all_user_model(self):
        self.cur.execute("SELECT * FROM users")
        result = self.cur.fetchall()
        return json.dumps(result)