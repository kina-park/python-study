import colorgram

# def color_tuple(image, n):
#     colors = colorgram.extract(image, n)
#
#     color_list = []
#     for i in range(n):
#         red = colors[i].rgb[0]
#         green = colors[i].rgb[1]
#         blue = colors[i].rgb[2]
#         color_list.append((red, green, blue))
#
#     return color_list
#
# print(color_tuple("hirst.jpg", 30))

colors_list = [(254, 253, 250), (247, 252, 250), (251, 242, 246), (229, 243, 249), (244, 230, 73), (195, 10, 67),
               (212, 156, 90), (20, 117, 173), (166, 170, 29), (107, 179, 208), (217, 131, 165), (161, 74, 31),
               (237, 72, 34), (27, 138, 72), (126, 181, 144), (6, 34, 88), (214, 82, 128), (82, 18, 82), (238, 222, 5),
               (175, 47, 88), (10, 58, 36), (13, 165, 212), (240, 161, 190), (122, 34, 22), (10, 45, 128),
               (52, 163, 120), (5, 102, 59), (141, 208, 217), (4, 88, 98), (159, 210, 187)]

import turtle

# 원 그리기 함수 정의
def draw_circle(x, y, radius):
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.circle(radius)

# 메인 함수
def main():
    # 원의 개수
    num_circles = 10

    # 원의 반지름
    radius = 20

    # 시작 좌표 설정
    x_start = -200
    y_start = 200

    # x, y 좌표 값 계산하여 원 그리기
    for i in range(num_circles):
        x = x_start + (2 * i * radius)
        for j in range(num_circles):
            y = y_start - (2 * j * radius)
            draw_circle(x, y, radius)

    # 그리기 완료 후 펜 숨기기
    turtle.hideturtle()

# 메인 함수 실행
main()

# 화면 유지
turtle.done()
