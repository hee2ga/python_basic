class Student:
    def __init__(self,name,korean,math,english,science):
        self.name=name
        self.korean=korean
        self.math=math
        self.english=english
        self.science=science
    
    def get_sum(self):
        return self.korean+self.math+self.english+self.science
    
    def get_average(self):
        return self.get_sum()/4
    
    def __str__(self):
        return "{}\t{}\t{}".format(self.name,self.get_sum(),self.get_average())
    
    def __eq__(self, value): # 같다(equal)
        return self.get_sum()==value.get_sum()
    def __ne__(self, value): # 다르다(not equal)
        return self.get_sum()!=value.get_sum()
    def __gt__(self, value): # 크다(greater than)
        return self.get_sum()>value.get_sum()
    def __ge__(self, value): # 크거나 같다(greater than or equal)
        return self.get_sum()>=value.get_sum()
    def __lt__(self, value): # 작다(less than)
        return self.get_sum()<value.get_sum()
    def __le__(self, value): # 작거나 같다(less than or equal)
        return self.get_sum()<=value.get_sum()
    
students=[
    Student("윤인성",87,98,88,95),
    Student("연하진",92,98,96,98),
    Student("구지연",76,96,94,90),
    Student("나선주",98,92,96,92),
    Student("윤아린",95,98,98,98),
    Student("윤명월",64,88,92,92),
]

student_a=Student("윤인성",87,98,88,95)
student_b=Student("연하진",92,98,96,98)

print("student_a == student_b = ",student_a==student_b)
print("student_a != student_b = ",student_a!=student_b)
print("student_a > student_b = ",student_a>student_b)
print("student_a >= student_b = ",student_a>=student_b)
print("student_a < student_b = ",student_a<student_b)
print("student_a <= student_b = ",student_a<=student_b)
        