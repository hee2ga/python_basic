import math

class Circle:
    def __init__(self,radius):
        self.__radius=radius
    
    def get_circumference(self):
        return 2*math.pi*self.__radius
    
    def get_area(self):
        return math.pi*(self.__radius**2)
    
    # 게터와 세터 선언
    def get_radius(self):
        return self.__radius
    
    def set_radius(self,value):
        self.__radius=value

circle=Circle(10)
print("# 원의 둘레와 넓이를 구합니다.")
print("원의 둘레 : ",circle.get_circumference())
print("원의 넓이 : ",circle.get_area())
print()

print("# __radius에 접근합니다.")
print(circle.get_radius()) # 게터 사용
print()
circle.set_radius(2) # 세터 사용

print("# 반지름을 변경하고 원의 둘레와 넓이를 구합니다.")
print("원의 둘레 : ",circle.get_circumference())
print("원의 넓이 : ",circle.get_area())