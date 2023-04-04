from service import db

# 테이블 별로 클래스를 설계
# 클래스 1개 -> 테이블 1개
# 클래스의 멤버 -> 테이블의 컬럼
# 클래스 객체 1개 -> 테이블의 row 데이터 1개

# 질문 테이블
class Question(db.Model):
    pass

# 답변 테이블
class Answer(db.Model):
    pass