import psycopg
from psycopg.rows import dict_row # 행을 어떤 형태로 만들지 정하는 방식, 기본값은 튜플인데, dict_row를 쓰면 row["course_name"]처럼 컬럼 이름으로 꺼낼 수 있음

# 데이터베이스에 접속하기 위한 정보를 한데 묶어 부르는 이름
# DSN : Data Source Name
DSN = "host=localhost port=5432 dbname=sportscenter user=postgres password=admin1234"


MONTH = "2026-11"

LIST_SQL = """
SELECT DISTINCT c.course_id, s.sport_name, c.course_name, c.class_days, c.fee
FROM courses c
JOIN sports s ON c.sport_id = s.sport_id
LEFT JOIN enrollments e ON c.course_id = e.course_id 
                        AND e.enroll_month = %s
ORDER BY c.course_id
"""

# 수강 신청가능 목록 조회
def list_courses(conn):
    for c in conn.execute(LIST_SQL, (MONTH,)):             #conn.execute(LIST_SQL, (MONTH, asdf, asdf)) 파라미터는 asdf처럼 입력하면 된다.
        print(f"{c['course_id']:>3} | {c['sport_name']} | {c['course_name']} | {c['class_days']} | {c['fee']}원")

# ☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★26-11-19 과제 내용 ☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★

# TODO: 입력 로직 구현
MEMBER_ID = 10
COURSE_ID = 1

# 수강신청
def enroll(conn, member_id, course_id):
    # TODO : 신청한 강좌의 수강료 추출
    fee = 0

    conn.execute(
        "INSERT INTO enrollments (member_id, course_id, enroll_month, status, pay_amount)"
        "VALUES (%s, %s, %s, '수강중', %s)",
        (member_id, course_id, MONTH, fee)
    )
    print("수강신청 완료되었습니다.")



def main():
    with psycopg.connect(DSN, row_factory=dict_row) as conn:                              # conn으로 축약해서 사용하겠단 선언
        # 수강신청
        enroll(conn, MEMBER_ID, COURSE_ID)
        
        # 수강 목록
        # list_courses(conn)


    
        # row = conn.execute("SELECT current_database(), current_user").fetchone()        # 실행하겠다는 뜻 (튜플의 형태로 파이썬에 데이터가 넘어감)
        # print("연결 성공:", row)
        # rows = conn.execute("SELECT course_id, course_name, fee FROM courses LIMIT 5").fetchall()
        # print(rows)
        # for row in rows:
        #     print(row["course_name"], row["fee"])


if __name__ == "__main__":
    main()