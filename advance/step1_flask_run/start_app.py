# 사용자가 정의한 엔트리 포인트
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello World start_app'