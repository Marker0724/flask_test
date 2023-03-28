'''
    메인 서비스를 구축하는 컨트롤러
    - 라우트 : URL과 이를 처리할 함수 연계
    - 비즈니스 로직 : 사용자가 요청하는 주 내용을 처리하는 곳
'''

from flask import render_template, request, redirect, url_for
from service.controllers import bp_main as main
from service.forms import FormQuestion

# ~/main/
@main.route('/')
def home():
    return render_template('index.html')

# ~/main/question
@main.route('/question', methods=['GET', 'POST'])
def question():
    form = FormQuestion()
    if request.method == 'POST' and form.validate_on_submit():
        return redirect(url_for('main_bp.home')) # ~/main
    return render_template('question.html', wtf=form)
