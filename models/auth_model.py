from datetime import datetime, timedelta
from logging import exception
import mysql.connector
import jwt
from flask import make_response, request, json
import re
class auth_model():
    
    def __init__(self):
        self.con = mysql.connector.connect(host="localhost",user="root",password="",database="test")
        self.con.autocommit=True
        self.cur = self.con.cursor(dictionary=True)
        
    def token_auth(self, endpoint):
        def inner1(func):
            def inner2(*args):
                authorization = request.headers.get("authorization")
                if re.match("^Bearer *([^ ]+) *$", authorization, flags=0):
                    token = authorization.split(" ")[1]
                    try:
                        tokendata = jwt.decode(token, "Sagar@123")
                    except jwt.ExpiredSignatureError:
                        return make_response({"ERROR":"TOKEN_EXPIRED"}, 401)
                    print(tokendata)
                    current_role = tokendata['payload']['roleid']
                    self.cur.execute(f"SELECT * FROM accessibility_view WHERE endpoint='{endpoint}'")
                    result = self.cur.fetchall()
                    if len(result)>0:
                        roles_allowed = json.loads(result[0]['roles_allowed'])
                        if current_role in roles_allowed:
                            return func(*args)
                        else:
                            return make_response({"ERROR":"INVALID_ROLE"}, 422)
                    else:
                        return make_response({"ERROR":"INVALID_ENDPOINT"}, 404)
                else:
                    return make_response({"ERROR":"INVALID_TOKEN"}, 401)
                
            return inner2
        return inner1