from urllib import request

targer=request.urlopen("https://www.hanbit.co.kr/images/common/logo_hanbit.png")
ouput=targer.read()
print(ouput)

file=open("output.png","wb") # 바이너리 형식으로 쓸때는 wb!
file.write(ouput)
file.close()