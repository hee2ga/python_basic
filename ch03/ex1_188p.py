import datetime

str_input=input("입력>")

now=datetime.datetime.now()
hour=now.hour


if "안녕" in str_input:
    print("안녕하세요.")

elif "몇시" in str_input:
    print("지금은 {}시 입니다.".format(hour))

else : print(str_input)