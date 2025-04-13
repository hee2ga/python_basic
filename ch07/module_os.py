import os

# 기본 정보 출력력
print("현재 운영체제 : ",os.name)
print("현재 폴더 : ",os.getcwd())
print("현재 폴더 내부의 요소 : ",os.listdir())

# 폴더 만들기
os.mkdir("hello")
# 폴더 제거하기
os.rmdir("hello")

# 파일 생성한 후 이름 변경
with open("original.txt","w") as file:
    file.write("hello")
os.rename("original.txt","new.txt")

# 파일 삭제
os.remove("new.txt")
# os.unlink("new.txt")

# 시스템 명령어 실행
os.system("dir")