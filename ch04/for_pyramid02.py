ouput=""

for i in range(1,15):
    for j in range(14,i,-1):
        ouput+=' '
    for k in range(0,2*i-1):
        ouput+='*'
    ouput+='\n'
print(ouput)