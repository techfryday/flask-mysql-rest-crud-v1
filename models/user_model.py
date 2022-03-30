import mysql.connector
import json
from flask import make_response, jsonify
class user_model():
    def __init__(self):
        self.con = mysql.connector.connect(host="localhost",user="root",password="123123",database="test")
        self.con.autocommit=True
        self.cur = self.con.cursor(dictionary=True)
        
    def all_user_model(self):
        self.cur.execute("SELECT * FROM users")
        result = self.cur.fetchall()
        if len(result)>0:
            print(type(result))
            return {"payload":result}
            # return make_response({"payload":result},200)
        else:
            return "No Data Found"
    
    def add_user_model(self,data):
        self.cur.execute(f"INSERT INTO users(name, email, phone, role, password) VALUES('{data['name']}', '{data['email']}', '{data['phone']}', '{data['role']}', '{data['password']}')")
        return make_response({"message":"CREATED_SUCCESSFULLY"},201)

    def delete_user_model(self,id):
        self.cur.execute(f"DELETE FROM users WHERE id={id}")
        if self.cur.rowcount>0:
            return make_response({"message":"DELETED_SUCCESSFULLY"},202)
        else:
            return make_response({"message":"CONTACT_DEVELOPER"},500)
        
    
    def update_user_model(self,data):
        self.cur.execute(f"UPDATE users SET name='{data['name']}', email='{data['email']}', phone='{data['phone']}' WHERE id={data['id']}")
        if self.cur.rowcount>0:
            return make_response({"message":"UPDATED_SUCCESSFULLY"},201)
        else:
            return make_response({"message":"NOTHING_TO_UPDATE"},204)

    def patch_user_model(self, data):
        qry = "UPDATE users SET "
        for key in data:
            if key!='id':
                qry += f"{key}='{data[key]}',"
        qry = qry[:-1] + f" WHERE id = {data['id']}"
        self.cur.execute(qry)
        if self.cur.rowcount>0:
            return make_response({"message":"UPDATED_SUCCESSFULLY"},201)
        else:
            return make_response({"message":"NOTHING_TO_UPDATE"},204)

    def pagination_model(self, pno, limit):
        pno = int(pno)
        limit = int(limit)
        start = (pno*limit)-limit
        qry = f"SELECT * FROM users LIMIT {start}, {limit}"
        self.cur.execute(qry)
        result = self.cur.fetchall()
        if len(result)>0:
            return make_response({"page":pno, "per_page":limit,"this_page":len(result), "payload":result})
        else:
            return make_response({"message":"No Data Found"}, 204)
        