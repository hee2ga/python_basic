numbers=[273,103,5,32,65,9,72,800,99]

for number in numbers:
    if number %2==0: print(f"{number}은 짝수입니다.")
    else : print(f"{number}은 홀수입니다.")

for number in numbers:
    print(f"{number}은 {len(str(number))}자릿수입니다.");