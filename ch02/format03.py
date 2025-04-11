# 기호와 함께 출력하기
output_f="{:+d}".format(52) # 양수의 경우 + 기호까지 출력
output_g="{:+d}".format(-52)
output_h="{: d}".format(52) # 양수의 경우 + 기호 부분 공백
output_i="{: d}".format(-52)

print("# 기호와 함께 출력하기")
print(output_f)
print(output_g)
print(output_h)
print(output_i)