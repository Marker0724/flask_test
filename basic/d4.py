'''
    데이터 베이스 접속 후 쿼리 수행 + 파라미터 전달
'''
import pymysql as my

def login_db(uid, upw) :
    '''
        아이디, 비밀번호를 넣어서 회원 여부를 체크하는 함수
        parameter
            - uid : 아이디
            - upw : 비밀번호
        retrun 
            - 회원인 경우
                - {'uid': 'guest', 'name': 'guest', 'regdate': datetime.datetime(2023, 3, 24, 13, 2, 30)}
            - 비회원인 경우, 디비측 오류
                - None
    '''
    connection = None
    row = None # 로그인 쿼리 수행 결과를 담는 변수
    try:
        connection = my.connect(host = 'localhost',
                                port = 3306,
                                user = 'root',
                                password = '12341234',
                                database = 'ml_db',
                                cursorclass = my.cursors.DictCursor
                                )

        with connection.cursor() as cursor :
            # 파라미터는 %s 표시로 순서대로 세팅된다. '값' -> ''는 자동으로 세팅된다.
            sql = '''
                SELECT 
                    uid, `name`, regdate
                FROM
                    users
                WHERE
                    uid=%s
                AND
                    upw=%s;
            '''
            # execute() 함수의 2번 인자가 파라미터 전달하는 자리, 튜플로 표현
            cursor.execute(sql, (uid, upw))
            row = cursor.fetchone() # 결과 셋 중 한개만 가져온다. -> 단수(리스트가 아닌 단독 타입 : 딕셔너리)
            #print(row['name'])
            pass 

    except Exception as e:
        print('접속 오류', e)

    else:
        print('접속 시 문제 없었다.')

    finally:
        if connection:
            connection.close()

    # 로그인한 결과 리턴 -> {...}
    return row

if __name__ == '__main__':
    # d4 개발자의 테스트 코드
    # f5 개발자가 사용할 때는 작동 안함
    # 정상계정
    print(login_db('guest', '1234'))
    # 비정상계정
    print(login_db('guest', '12345'))