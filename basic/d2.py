'''
    데이터 베이스 접속 후 쿼리 수행
'''
import pymysql as my

connection = None

try:
    connection = my.connect(host = 'localhost',
                            port = 3306,
                            user = 'root',
                            password = '12341234',
                            database = 'ml_db',
                            # 조회 결과는 [{}, {}, {}, ...] 형태로 추출된다.
                            # 사용 안하면 [(, ), (, ), (, ), ...] 형태로 추출된다.
                            #cursorclass = my.cursors.DictCursor
                            )
    # 쿼리 수행
    # pymysql은 커서를 획득해서 쿼리를 수행한다. -> Rule
    # 1. 커서 획득
    #connection.cursor(my.cursors.DictCursor)
    with connection.cursor() as cursor :
        # 2. sql문 준비
        sql = '''
            SELECT 
                uid, `name`, regdate
            FROM
                users
            WHERE
                uid='guest'
            AND
                upw='1234';
        '''
        # 3. sql 쿼리 수행
        cursor.execute(sql)
        # 4. 결과를 획득
        row = cursor.fetchone()
        # 5. 결과 확인 -> 튜플 -> 이름만 추출하시오 -> 순서가 중요, 인덱싱 -> 'guest'
        # 튜플로 결과를 받는 것은 결과값의 순서가 바뀌지 않는다는 전제하에서 가능
        # 유연하게 대처하고 싶다면 -> 컬럼 순서가 변경되던, 쿼리문의 순서가 변경되던지 -> 관계없이 대응
        # 순서 없는 자료구조 -> 딕셔너리 -> d3.py
        print(row[1])
        pass 

except Exception as e:
    print('접속 오류', e)

else:
    print('접속 시 문제 없었다.')

finally:
    if connection:
        connection.close()

