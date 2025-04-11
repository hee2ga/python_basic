min=2
max=10
total=100
memo={}

def solution(left,seated):
    key=str([left,seated])

    if key in memo:
        return memo[key]
    if left<0:
        return 0
    if left==0:
        return 1
    count=0
    for i in range(seated,max+1):
        count+=solution(left-i,i)
    memo[key]=count
    return count

print(solution(total,min))