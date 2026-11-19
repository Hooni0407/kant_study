# # 클래스 정의(선언) : 붕어빵 틀
# class User:
#     def __init__ (self, name): # 생성자 : 클래스가 처음 생성될 때 자동으로 호출
#         self.name = name # 변수를 초기화

#     def show(self): # 메서드(Method)
#         return f"회원 이름: {self.name}"

# # 인스턴스 생성 : 붕어빵 만들기
# user_a = User("손흥민")
# user_b = User("이강인")

# # User 클래스로 생성한 인스턴스 (메모리에 생성)

# # 클래스의 인스턴스 변수
# print(user_a.name)
# print(user_b.name)

# # 클래스의 메서드 접근
# print(user_a.show())
# print(user_b.show())


# print(type(user_a))
# print(user_a is user_b)
# print(id(user_a))
# print(id(user_b))

# #===================================================================================================================================================

# class Monitor:
#     def display_info(self):
#         # 인스턴스 변수
#         self.resolution = "1920X1080"
#         self.size = "27인치"
#         print(f"모니터 정보\n해상도: {self.resolution}\n해상도: {self.size}\n객체 ID : {id(self)}")

# monitor = Monitor() # 인스턴스 생성
# print(id(monitor)) # 모니터 인스턴스 ID 출력

# monitor.display_info()

# #===================================================================================================================================================

# class SmartPhone:
#     def __init__(self, model):
#         self.model = model # 속성 (Attribute)
#         self.battery = 50 # 속성 (Attribute)

#     def charge(self, amount):
#         self.battery += amount
#         if self.battery > 100:
#             self.battery = 100
#             print(f"배터리 충전 완료 : {self.battery}%")
#         else:
#             print(f"배터리 충전 중 ... : {self.battery}%")

# phone_a = SmartPhone("아이폰")
# print(phone_a.model)
# phone_a.charge(30)
# phone_a.charge(30)

# phone_b = SmartPhone("갤럭시")
# print(phone_b.model)
# phone_b.charge(30)
# phone_b.charge(30)

# 은행 계좌 클래스
# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner          # 계좌 예금주
#         self.balance = balance

#     def __str__(self):
#         return f"예금주 : {self.owner}, 잔액 : {self.balance:,}"

#     def __repr__(self):
#         return f"예금주 : {self.owner}, 잔액 : {self.balance:,}"

#     # 입금 처리 메서드
#     def deposit(self, amount):
#         self.balance += amount # 입금처리
#         print(f"{amount:,}원 입금완료 //// 잔액 : {self.balance:,}원")

#     # 출금 메서드
#     # 잔액 확인 - 잔액 부족 메시지 출력

#     def withdraw(self, amount):
#         # 잔액 확인
#         if self.balance < amount:
#             print(f"잔액 부족")
#             return 0

#         self.balance -= amount
#         print(f"{amount:,} 출금 처리")
#         return self.balance # 출금 후 잔액 리턴


# account_a = BankAccount("이승훈", 100_000)  # 변수 선언
# print(account_a)                            # 예금주, 잔액 확인
# account_a.deposit(500_000)                  # 입금 처리 출력

# account_a.withdraw(1_000_000)                 # 출금 처리 출력

# print(f"잔액: {account_a.withdraw(200_000)}")

# print(f"잔액: {account_a.withdraw(300_000)}")

# account_c = BankAccount("홍길동", 200_000)
# print([account_a, account_c])
























































#=====================================================================================================================================================
import random

# 제목 출력
print("=" * 40)
print("가위 / 바위 / 보")
print("=" * 40)
print("1. 가위 / 2. 바위 / 3. 보")


# 변수 선언
game_count = 0
my_score = 0
com_score = 0
player_name = str(input("플레이어 이름을 입력하세요. :"))
player_list = []
my_number = int(input("번호를 선택하세요. : "))


# 플레이어 이름 입력 받고 승패 기록 표시
def game_win_lose_record():
    global player_name
    global player_list
    global win_lose
    player_list.append(player_name)
    player_list.append(win_lose)
    print(f"플레이어 : {player_name}, {win_lose}")


# 나 가위바위보 변수 지정
def my_srp():
    global my_number
    if my_number == 1:
        srp = ("가위")
    elif my_number == 2:
        srp = ("바위")
    else:
        my_number == 3
        srp = ("보")
    return srp
# 컴퓨터 가위바위보 변수 지정
def com_srp():
    global com_number
    if com_number == 1:
        srp = ("가위")
    elif com_number == 2:
        srp = ("바위")
    else:
        com_number == 3
        srp = ("보")
    return srp
# ====================================================================================
print("[게임 결과]")
while True:
    com_number = random.randint(1, 3)
    # 게임 누가 이겼나~~
    if my_number == 1 and com_number == 2:
        print(f"나 : {my_srp()} vs 컴퓨터 : {com_srp()}")
        print("패배")
        win_lose = "패배"
        game_count += 1
        com_score += 1
    elif my_number == 2 and com_number == 3:
        print(f"나 : {my_srp()} vs 컴퓨터 : {com_srp()}")
        print("패배")
        win_lose = "패배"
        game_count += 1
        com_score += 1
    elif my_number == 3 and com_number == 1:
        print(f"나 : {my_srp()} vs 컴퓨터 : {com_srp()}")
        print("패배")
        win_lose = "패배"
        game_count += 1
        com_score += 1
    # 여기부턴 "나"가 이기는 경우
    elif com_number == 1 and my_number == 2:
        print(f"나 : {my_srp()} vs 컴퓨터 : {com_srp()}")
        print("승리")
        win_lose = "승리"
        game_count += 1
        my_score += 1
    elif com_number == 2 and my_number == 3:
        print(f"나 : {my_srp()} vs 컴퓨터 : {com_srp()}")
        print("승리")
        win_lose = "승리"
        game_count += 1
        my_score += 1
    elif com_number == 3 and my_number == 1:
        print(f"나 : {my_srp()} vs 컴퓨터 : {com_srp()}")
        print("승리")
        win_lose = "승리"
        game_count += 1
        my_score += 1
    # 여기부턴 비기는 경우
    else:
        com_number == my_number
        print(f"나 : {my_srp()} vs 컴퓨터 : {com_srp()}")
        print("비김")
        win_lose = "비김"
        game_count += 1

    print(f"현재 스코어 <나> {my_score} : {com_score} <컴퓨터>")

    game_win_lose_record() # 플레이어의 승패기록

    # 재도전 문장 출력
    # 사용자 입력받기
    # 문자로 if절로 판단
    # True → continue
    # False → break

    if my_score == 2 or com_score == 2:
        print(input("재도전 하시겠습니까?(y or n) : "))
        regame = input()
        if regame == "y":
            break
    