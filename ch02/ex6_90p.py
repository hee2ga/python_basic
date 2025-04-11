# 스왑을 이용한 변수값 교체

str_a=input("문자열 입력 >")
str_b=input("문자열 입력 >")

print("스왑 전")
print(str_a,str_b)

print("스왑 후")
terms=str_a
str_a=str_b
str_b=terms
print(str_a,str_b)