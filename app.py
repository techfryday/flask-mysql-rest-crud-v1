from flask import Flask

app = Flask(__name__)

try:
    from controllers import *
except Exception as e:
    print(e)


