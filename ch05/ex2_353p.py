numbers=list(range(1,10+1))

print("# 홀수만 추출하기")
print(list(filter(lambda x:x%2==1,numbers)))

print("# 3이상 7미만 추출하기")
print(list(filter(lambda x:3<=x<7,numbers)))

print("# 제곱해서 50미만 추출하기")
print(list(filter(lambda x:x**2<50,numbers)))