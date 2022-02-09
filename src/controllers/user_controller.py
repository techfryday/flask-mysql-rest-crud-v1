from src import app
@app.route("/user/all")
def all_users():
    return "hi All Users, How are you"


