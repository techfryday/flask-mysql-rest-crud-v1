from flask import Flask
sagar="hi"
app = Flask(__name__)
print(__name__)
@app.route("/home")
def home():
    return "This is home"

import src.controllers.user_controller