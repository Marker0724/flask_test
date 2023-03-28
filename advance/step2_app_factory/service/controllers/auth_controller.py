'''
    메인 서비스를 구축하는 컨트롤러
    - 라우트 : URL과 이를 처리할 함수 연계
    - 비즈니스 로직 : 사용자가 요청하는 주 내용을 처리하는 곳
'''

from flask import render_template, request, url_for
from service.controllers import bp_auth as auth


@auth.route('/')
def home():
    # url_for(별칭.함수명) => url이 리턴된다.
    print(url_for('auth_bp.login'))
    return '인증 홈'

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        # jwt 관련 체크 -> 정상(200), 오류(401)
        return 'jwt 체크 완료'

@auth.route('/logout')
def logout():
    return '로그아웃 홈'

@auth.route('/sighup')
def sighup():
    return '회원가입 홈'

@auth.route('/delete')
def delete():
    return '회원탈퇴 홈'