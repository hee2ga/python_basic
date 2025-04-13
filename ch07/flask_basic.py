from flask import Flask
app=Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello World!</h1>"

# 실행시 터미널에 $env:FLASK_APP="ch07/flask_basic" flask run 입력