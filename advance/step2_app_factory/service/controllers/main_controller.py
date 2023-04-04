'''
    메인 서비스를 구축하는 컨트롤러
    - 라우트 : URL과 이를 처리할 함수 연계
    - 비즈니스 로직 : 사용자가 요청하는 주 내용을 처리하는 곳
'''
# 환경변수의 시크릿 키 획득을 위해서 Falsk 객체를 획득
from flask import render_template, request, redirect, url_for, current_app, Response
from service.controllers import bp_main as main
from service.forms import FormQuestion
import jwt
# 시간 관련
import time
from datetime import datetime


# ~/main/
@main.route('/')
def home():
    # 1. 쿠키중에 토큰 획득 -> 실패 -> 401
    token = request.cookies.get('token')
    SECRET_KEY = current_app.config['SECRET_KEY']
    print(token, SECRET_KEY)
    if not token or not SECRET_KEY:
        return Response(status=401)
    try:
        # 2. 디코딩 -> 실패하면 -> 401
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        # 3. 유효 날짜 추출, 현재 시간 기준보다 과거인지 체크 -> 과거라면
        if payload['exp'] < time.mktime(datetime.utcnow().timetuple()): # 현재 시간보다는 과거
            return Response(status=401)
        # 4. 정상
        return render_template('index.html')
    except jwt.InvalidTokenError:
        return Response(status=401)
    except jwt.ExpiredSignatureError:
        return Response(status=401)
    except jwt.exceptions.DecodeError:
        return Response(status=401)

# ~/main/question
@main.route('/question', methods=['GET', 'POST'])
def question():
    form = FormQuestion()
    if request.method == 'POST' and form.validate_on_submit():
        return redirect(url_for('main_bp.home')) # ~/main
    return render_template('question.html', wtf=form)
