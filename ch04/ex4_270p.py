pre_list=[1,2,[3,4],5,[6,7],[8,9]]

result=[]

for i in pre_list:
    if type(i)==list :
        for j in i:
            result.append(j)
    else:
        result.append(i)

print(result)
