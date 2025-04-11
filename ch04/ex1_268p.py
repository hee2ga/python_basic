test=[1,2,3,4,1,2,3,1,4,1,2,3]
value={}

for i in test:
    if i not in value:
        value[i]=0
    value[i]+=1
print(f"{test}에서 사용된 숫자의 종류는 {len(value)}개입니다.")