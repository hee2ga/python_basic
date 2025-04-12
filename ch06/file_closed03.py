try:
    file=open("ch05/info.txt","w")
    예외.발생()
except:
    print("오류가 발생했습니다.")
finally:
    file.close()

print("# 파일 제대로 닫혔는지 확인하기")
print("file.closed : ",file.closed)