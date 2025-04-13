def test(function):
    def wrapper(): # 실제로 실행되는 함수
        print("인사가 시작되었습니다.")
        function()
        print("인사가 종료되었습니다.")
    return wrapper

@test
def hello():
    print("hello")

hello()
