from src import app
from src.models.user_model import user_model
obj = user_model()
@app.route("/user/all")
def all_users():
    return obj.all_user_model()


