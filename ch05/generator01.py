def test():
    print("A 지점 통과")
    yield 1
    print("B 지점 통과")
    yield 2
    print("C 지점 통과")

ouput=test()
print("D 지점 통과")
a=next(ouput)
print(a)
print("E 지점 통과")
b=next(ouput)
print(b)
print("F 지점 통과")
c=next(ouput)
print(c)

next(ouput)