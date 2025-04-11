# inch 단위의 자료를 입력받아 cm  단위를 구하는 예제
# 1 inch = 2.54cm

str_inch=input("inch를 입력해주세요>")
float_inch=float(str_inch)
cm=float_inch*2.54

print("cm로 변환한 결과 : ",cm,"cm")