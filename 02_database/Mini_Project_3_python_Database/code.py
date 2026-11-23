import psycopg
from psycopg.rows import dict_row

DSN = "host=localhost port=5432 dbname=sportscenter user=postgres password=admin1234"

ID_S_SQL = """
SELECT member_id
FROM members
WHERE name = %s;
"""

COURSE_ID = 1


# 1. 회원 이름으로 회원 ID 조회
def id_select(conn, name):
    row = conn.execute(ID_S_SQL, (name,)).fetchone()
    if row is None:
        print("데이터가 비었습니다.")
        return None        
    return row["member_id"]

# 2. 신청 강좌의 수강료 조회
def fee_select(conn, member_id, course_id):
    fee = 0
    conn.execute(
        "INSERT INTO enrollments (member_id, course_id, fee)"
        VALUES (%s, %s, %s, '')
    )

    
def main():
    with psycopg.connect(DSN, row_factory=dict_row) as conn:
        name = input("회원 이름: ").strip()
        member_id = id_select(conn, name)
        print(member_id)

if __name__ == "__main__":
    main()