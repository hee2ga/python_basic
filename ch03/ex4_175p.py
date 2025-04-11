a=float(input("첫번째 숫자 입력 >"))
b=float(input("두번째 숫자 입력 >"))
print()

if a>b:
    print("처음 입력했던 {}가 {}보다 크다".format(a,b))

if a<b:
    print("두번째로 입력했던 {}가 {}보다 크다".format(b,a))