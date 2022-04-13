from flask import Flask

app = Flask(__name__)

try:
    from controllers import *
except Exception as e:
    print(e)


# def token_auth(endpoint):
#     def inner1(func):
#         def inner2(*args):
#             print("This is inner 2")
#             func(*args)
#         return inner2
#     return inner1

# @token_auth("/user/all")
# def somefun():
#     print("Something")

# somefun()
