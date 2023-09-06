# # STMP; Simple Mail Transfer Protocol
# import smtplib
#
# my_email = "qkrrlsk8062@gmail.com"
# password = "mgwewjxekprnswtv" # 구글 계정 > 보안 > 2단계 인증 > 앱 비밀번호  > gmail
#
# with smtplib.SMTP("smtp.gmail.com") as connection:  # 객체 생성시 이메일 제공자의 SMTP 서버 위치 지정
#     connection.starttls()  # tls; transport layer security -> 이메일 서버와의 연결을 안전하게 만드는 방식
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="qkrrlsk8062@yahoo.com",
#         msg="Subject:Hello\n\nThis is the body of the email."
#     )
import smtplib
import datetime as dt
import random

now = dt.datetime.now()  # # type(now) -> class
year = now.year  # type(year) -> int
month = now.month
day_of_week = now.weekday() # 주중의 몇 번째 날인지 ex) 2 = 수

date_of_birth = dt.datetime(year=1995, month=7, day=29)  # 파라미터 확인해 보면, hour : int=..., 기본값 설정되어 있다는 뜻.
# print(date_of_birth)  # 1995-07-29 00:00:00

# TODO: 1. quotes.txt 파일의 모든 줄을 리스트로 만들기
with open("quotes.txt", "r") as file:
    quotes_list = file.readlines()

# TODO: 2. 오늘이 몇 요일인지 확인하고, 맞으면 무작위 명언이 담긴 이메일 전송하기
my_email = "qkrrlsk8062@gmail.com"
password = "mgwewjxekprnswtv"
random_quote = random.choice(quotes_list)

if day_of_week == 2:
    with smtplib.SMTP("smtp.gmail.com") as connection:  # 객체 생성시 이메일 제공자의 SMTP 서버 위치 지정
        connection.starttls()  # tls; transport layer security -> 이메일 서버와의 연결을 안전하게 만드는 방식
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="qkrrlsk8062@naver.com",
            msg=f"Subject:Tuesday Motivation\n\n{random_quote}"
        )

