# 함수 input()과 int()활용

planet = input('원하는 행성은? ')
strRadius = input(planet + '의 반지름은?')
radius = int(strRadius)

length = 2*3.14*int(strRadius)
print(planet,'반지름:',radius)
print(planet,'둘레길이:',length)