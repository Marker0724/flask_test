# 풀링 기법 적용
import sqlalchemy.pool as pool
import pymysql
from flask import current_app

# 커넥션 풀을 관리하는 객체 (전역변수)
db_pool = None

# 커넥션 처리 함수
def get_conn():
    c = pymysql.connect(host='localhost',
                        user='root',
                        password='12341234',
                        database='ml_db',
                        cursorclass=pymysql.cursor.DictCursor)
    return c

# 풀링 생성 함수
def init_pool():
    global db_pool
    '''
        pool_size : 현재 구성상, 생상한 커넥션 수, 가장 작은 값(최소 단위)
        max_overflow : 물리적으로 버틸 수 있는 최대값으로 설정(최대 동시 처리 수)
    '''
    db_pool = pool.QueuePool(get_conn, max_overflow=10, pool_size=5)
    

# 로그인 처리
def login(uid, upw):
    row = None
    print('풀링에서 관리하는 커넥션 수 : ', db_pool.size())
    # 커넥션 풀에서 커넥션 1개를 빌려와서 -> 쿼리 수행 -> 반납
    # 1. 커넥션 획득
    conn = db_pool.connect()
    # 2. cursor 획득
    with conn.cursor() as cursor:
        sql = '''
            select
                *
            from
                users
            where
                uid=%s and upw=%s;
        '''
        cursor.execute(sql, (uid, upw))
        row = cursor.fetchone()
    # 3. 반납
    conn.close()
    return row