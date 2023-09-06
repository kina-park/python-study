# *args: Many Positional Arguments

# unlimited arguments
# 아래와 같이 함수가 있을 때,
def add(n1, n2):
    return n1 + n2

# 두 개 숫자 말고 더 여러 개의 숫자를 더하는 함수를 만들고 싶다면?
def add2(*args):
    # args의 type은 튜플. 따라서, 인덱스 접근도 가능.
    # 아스테리크를 사용한 가변 인수는 unlimited positional arguments 라고 불림.
    # print(args[0])
    sum = 0
    for n in args:
        sum += n
    return sum

# **kwargs: Many keyworded arguments
# 이중 아스테리크 연산자를 사용해서 "많은 선택적 키워드 인수를 갖는" 클래스를 생성
# 객체에 대해 초기화하고 싶은 것들이 무엇인지에 따라 선택적으로 설정하고 싶은 것을 추가할 수 있음
# 모든 선택 사항을 선택할 수도, 그냥 디폴트 값으로 놔둔채 사용할 수도 있음
def calculate(n, **kwargs):
    # kwargs의 type은 딕셔너리.
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)

class Car:

    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]

my_car = Car(make="Nissan", model='GT-R')
print(my_car.make)

class Car2:

    def __init__(self, **kw):
        # get 함수 사용
        # 딕셔너리의 key 이름을 전달해서 해당 value 값을 가져옴.
        # 딕셔너리에 key가 존재하지 않아도, 아무것도 반환을 안 하고 오류를 발생시키지 않는다는 이점이 있음.
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")

my_car2 = Car2(make="Nissan")
print(my_car2.model)
