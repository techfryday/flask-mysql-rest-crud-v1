import flask
from flask import request
from app import app
from models.user_model import user_model
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