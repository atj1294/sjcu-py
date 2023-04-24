######################################33
# 파이썬 함수 사용의 예


# 파라미터도 없고 리턴값도 없음
def hello():
    print("Hello World")


hello()


# 파라미터와 리턴값이 있음
def add(x, y):
    print(x)
    print(y)
    return x + y


val_x = 1
val_y = 2
val_sum = add(val_x, val_y)
print(val_sum)
