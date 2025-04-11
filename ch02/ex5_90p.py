# 원의 반지름을 입력받아 원의 둘레와 넓이를 구하는 코드
# 둘레 : 2 * 원주율 * 반지름
# 넓이 : 원주율 * 반지름 * 반지름

str_r=input("원의 반지름 입력 > ")
float_r=float(str_r)

print("원의 반지름 : ",float_r)
print("원의 둘레 : ",2*3.14*float_r)
print("원의 넓이 : ",3.14*float_r**2)
