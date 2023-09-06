# def add2(*args):
#     # args의 type은 튜플. 따라서, 인덱스 접근도 가능.
#     # 아스테리크를 사용한 가변 인수는 unlimited positional arguments 라고 불림.
#     # print(args[0])
#     sum = 0
#     for n in args:
#         sum += n
#     print(args)
#     return sum
#
# print(add2(1, 2, 3))

# def calculate(n, **kwargs):
#     # kwargs의 type은 딕셔너리.
#     print(kwargs)
#     # for key, value in kwargs.items():
#     #     print(key)
#     #     print(value)
#     n += kwargs.get("add")
#     n *= kwargs.get("multiply")
#     print(n)
#
# calculate(n=1, add=2)

def calculate(n, **kwargs):
    add_value = kwargs.get("add", 0)  # kwargs["add"]에 해당하는 value 없으면 해당 값을 0으로 설정해주기
    multiply_value = kwargs.get("multiply", 1)

    n += add_value
    n *= multiply_value
    print(kwargs)
    return n

print(calculate(n=2, add=3))
