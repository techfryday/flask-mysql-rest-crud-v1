import mysql.connector
import json
class user_model():
    def __init__(self):
        self.db = mysql.connector.connect(host="localhost",user="root",password="",database="test")
        self.cur = self.db.cursor(dictionary=True)
        
    def all_user_model(self):
        self.cur.execute("SELECT * FROM users")
        result = self.cur.fetchall()
        print(result)
        return json.dumps(result)
    
    def add_user_model(self,data):
        self.cur.execute(f"INSERT INTO users(name, email, phone, role, password) VALUES('{data['name']}', '{data['email']}', '{data['phone']}', '{data['role']}', '{data['password']}')")
        return data