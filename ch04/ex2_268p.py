input=input("염기 서열을 입력해주세요>")

counter={
    "a":0,
    "t":0,
    "g":0,
    "c":0
}

for i in input:
    if i not in input: 
        counter[i]=0
    else : counter[i]+=1
print(counter)
        

