# 사용자가 정의한 엔트리 포인트
from flask import Flask, render_template

'''
    create_app은 플라스크 내부에서 정의된 함수 명(수정 X)
    flask run을 수행하면 내부적으로 엔트리포인트 모듈에서 create_app()를 찾는다.
    차후, 다른 모듈에서는 flask.current_app 이라는 변수로 app을 접근할 수 있다.(모듈 가져오기)
'''

def create_app():
    app = Flask(__name__)

    init_blueprint(app)
    
    return app

def init_blueprint(app):
    # app에 블루프린트 객체를 등록한다.

    # 실습 http://127.0.0.1:5000/auth/ 접속 시 인증 홈이란 내용이 나오도록
    # auth 관련 블루 프린트를 구성하시오

    # 블루 프린트로 정의된 개별 페이지 관련 내용 로드
    from .controllers import main_controller
    from .controllers import auth_controller

    # 이 위치에서는 service를 생략하고 표현 가능
    from .controllers import bp_main, bp_auth

    # 플라스크 객체에 블루 프린트 등록
    app.register_blueprint(bp_main)
    app.register_blueprint(bp_auth)
    pass