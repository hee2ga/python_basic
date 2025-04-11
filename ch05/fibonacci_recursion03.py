counter=0

def fibonacci(n):
    global counter
    counter+=1
    if n==1: return 1
    if n==2: return 1
    else : return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(10))