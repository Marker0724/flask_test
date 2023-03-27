from flask import Blueprint

# 메인 서비스 페이지 - A 개발자 담당 -> 담당하는 모든 URL은 ~/main/~
bp_main = Blueprint('main_bp', # 별칭, 해당 블루프린트 밑에서 정의된 라우트 및 함수를 url_for('main_bp.home')로 지칭할 때 사용
                    __name__, # 고정
                    url_prefix='/main', # 모든 URL 앞에 /main이 추가된다.
                    template_folder='../templates', # html이 위치한 경로
                    static_folder='../static' # 정적데이터의 위치 경로
                    )

bp_auth = Blueprint('auth_bp', 
                    __name__, 
                    url_prefix='/auth',
                    template_folder='../templates',
                    static_folder='../static'
                    )
