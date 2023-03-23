'''
    클라이언트가 서버에게 데이터를 보내는 방법
    - 방법 : method : GET, POST, PUT, ... <- http(or https) 프로토콜(통신규약, 서로 데이터를 주고받는 약속)에서 정의
        http는 헤더(고정 크기)를 먼저 전송, 바디(가변크기)를 나중에 전송
        GET 방식은 헤더만 전송 -> 고정 크기만 전송 -> 보낼 양이(최대치가) 정해져 있다. -> 
            소량만 전송 http 헤더만 알면, 패킷(전송 데이터)를 가로채서 데이터를 해킹할 수 있다 -> 보안 취약
        POST 방식은 헤더(바디의 크기가 세팅되어 있음) 전송 -> 바디 전송 -> 대량 전송 가능, 구조를 모르기 때문에 보안에 상대적으로 우수, 암호화 가능 -> 보안이 상대적으로 양호하다.

    - 방식
        - form 전송 : <form> 태그 사용, 화면이 깜빡(순식 간 진행, x자로 주소창 앞에 아이콘이 변경)
        - ajax 전송 : 백그라운드로 서버와 통신, 화면은 고정
        - websocket : 웹 소켓을 열어서 통신
        - 동적 파라미터 : get의 헤더를 활용하여 URL에 데이터를 넣어서 보내는 방식
    
    - 동적파라미터
        - HTTP 헤더의 주소 정보를 활용
'''
from flask import Flask, render_template, jsonify, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    return 'Hello World'

# 동적 파라미터, 문자열 타입으로 전송
# 용량은 헤더 사이즈, 주소 크기를 초과할 수 없다.
# 파라미터는 함수 인자를 통해서 함수 내부로 진입
# #, <, >는 전달 안됨, 한글, 특수, 영대, 영소 다 가능
# URL 인코딩으로 전달하면 모두 전달 가능 %12%ae...
@app.route("/news/<news_id>")
def news(news_id):

    return '전달된 데이터 [%s]' % news_id

# URL을 무한대로 생산할 수 있다.
# 1개 이상도 전달 가능한가?, 위치 조정
# http://127.0.0.1:5000/ajbjan/news2/uasgdjhkbjn
@app.route("/<news_id>/news2/<news_author>")
def news2(news_id, news_author):

    return '전달된 데이터 [%s][%s]' % (news_id, news_author)

# 타입 제한이 가능한가? int, float, path
# http://127.0.0.1:5000/news3/123 -> 200 OK
# http://127.0.0.1:5000/news3/hello -> 404 
@app.route("/news3/<int:news_id>")
def news3(news_id):

    return '전달된 데이터 [%s]' % news_id
    
# path
# 전달값을 무한대로 늘려주는 옵션
# http://127.0.0.1:5000/news4/1/2/3/4/5/6/7/8/9/home/동국/10
@app.route("/news4/<path:news_id>")
def news4(news_id):
    # 정보를 구분해서 여러개로 전달 가능(가변적)
    return '전달된 데이터 [%s]' % news_id

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)