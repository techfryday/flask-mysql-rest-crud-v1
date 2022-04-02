import flask
from flask import request, send_file
from app import app
from models.user_model import user_model
import os
from datetime import datetime
obj = user_model()

@app.route("/user/all")
def all_users():
    # res = flask.Response(obj.all_user_model())
    # res.headers["Content-type"] = "application/json"
    return obj.all_user_model()

@app.route("/user/add", methods=["POST"])
def add_user():
    return obj.add_user_model(request.form)

@app.route("/user/delete/<id>", methods=["DELETE"])
def delete_user(id):
    return obj.delete_user_model(id)

@app.route("/user/update", methods=["PUT"])
def update_user():
    return obj.update_user_model(request.form)

@app.route("/user/patch", methods=["PATCH"])
def patch_user():
    return obj.patch_user_model(request.form)

@app.route("/user/page/<pno>/limit/<limit>", methods=["get"])
def pagination(pno, limit):
    return obj.pagination_model(pno, limit)

@app.route("/user/<uid>/avatar/upload", methods=["PATCH"])
def upload_avatar(uid):
    file = request.files['avatar']
    root_dir = os.path.dirname(app.instance_path)
    new_filename =  str(datetime.now().timestamp()).replace(".", "")
    split_filename = file.filename.split(".") 
    ext_pos = len(split_filename)-1
    ext = split_filename[ext_pos]
    db_path = f"/uploads/{new_filename}.{ext}"
    file.save(f"{root_dir}/uploads/{new_filename}.{ext}")
    return obj.upload_avatar_model(uid, db_path)

@app.route("/user/avatar/<uid>", methods=["GET"])
def get_avatar(uid):
    data = obj.get_avatar_path_model(uid)
    root_dir = os.path.dirname(app.instance_path)
    return send_file(f"{root_dir}{data['payload'][0]['avatar']}")