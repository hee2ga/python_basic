try:
    file=open("ch05\info.txt","w")
    file.close()
except:
    print("오류가 발생했습니다.")

print("# 파일이 제대로 닫혔는지 확인하기")
print("file.closed : ",file.closed)