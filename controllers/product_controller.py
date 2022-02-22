from app import app
@app.route("/product/all")
def all_product():
    return "All Product"
