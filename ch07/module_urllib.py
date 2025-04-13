from urllib import request

# urlopen() 함수로 구글의 메인페이지를 읽습니다.
target=request.urlopen("https://www.google.com")
output=target.read()

print(output)