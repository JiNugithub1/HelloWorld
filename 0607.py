# 0607 시험범위 정리


# 딕셔너리(dictionary)

# key - value ex) apple : 빨강,  banana : 노랑
# carDict = {key1 : value1 ,  key2 : value2,  key3 : value3}
# 자동차 등록번호: (생산년도, 배기량) :
list1 = [10,20,30,40,50,6]
carDict = {'h101' : ('2020','1600'), 'h102' : ('2021','2000'),
           'b101' : ('2020','3600'), 'b102' : ('2021','5200')}

# print(carDict.keys()) # key값만 뽑는 함수

# print(carDict.values()) # values값들만 뽑는 함수

# print(carDict.items())

# print(carDict)
'''
for item in carDict.items() :
    print(item[0], item[1])

for key in carDict.keys() :
    print(key, carDict[key])

'''
'''
yearlist=[]

for item in carDict.values() :
    yearlist.append(int(item[0]))

print(yearlist)
'''
'''
# 첫 번째 방법
year = input("생산년도를 입력하세요 : ") #2020
yearlist=[]

for item in carDict.values() :
    yearlist.append(int(item[0]))

print(year,"년도에 생산된 자동차는 ",yearlist.count(int(2020)),"대 입니다.")

#2 두번째 방법

count = 0
year2 = input("생산년도를 입력하세요 : ") #2020
for product in yearlist :
    if product == year2 :
        count +=1

print(count)
'''
'''
members = {'홍':'111', '박':'222','정' : '333'}
members['최'] = '555'
members.update({'강':'666'})
members['김'] = '777'
members.update({'최':'888'})
print(members)

'''
'''
L1 = [1,2,3,4,5]
L2 = ['a','b','c','d','e']

print(list(zip(L1,L2)))
# result : [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]



sports = ['축구','야구','농구','배구']
num = [11,9,5,6]

sportsnum = {}
sportsnum = dict(zip(sports,num))

print(sportsnum)


while 1 :
    s = input("구기종목을 입력하시오.")
    if s == 'quit' :
        break
    elif s in sportsnum.keys() :
        print("인원은",  sportsnum[s],"입니다.")
    else :
        print("몰라요")
        continue
        
'''
#-----------------------------------------------------------------
# 7장
# lambda 
#  filter와 lambda를 사용하여
# 리스트 [1,-2,3,-4,5,8,-3]에서 음수를 모두 제거해보자.

# list3 = [1,-2,3,-5,8,-3]
# def positivel1(x) :
#     return x>0
# lambda 입력값 : 리턴 결과

#filter(함수, 리스트)
# print(list(filter(positivel1,[1,-2,3,-5,8,-3])))
# print(list(filter(lambda x : x>0 ,[1,-2,3,-5,8,-3])))

# 숫자 리스트를 두 개를 받음
# 각각 같은 순서끼리 더하는 함수를 만들어라
# lambda와 map을 써서 작성해라

list4 = [10,20,30,40,50]
list5 = [100,200,300,400,500]


def mysum(n1,n2) :
    return n1+n2

print(list(map(mysum,list4,list5)))
print(list(map(mysum,[10,20,30,40,50],[100,200,300,400,500])))
#lambda
print(list(map(lambda n1,n2 : n1+n2, list4, list5)))

#----------------------------------------------------------------------
# 9장
'''
from xxxx import xxx as x
   -> 형태는 이런식으로 구성되어 있다.
1. py - ___name___ =1 run
2. py - __name__ = 해당파일이름 , 2
3. py - __name__ = 3
'''

print("2.py입니다.")
print("__name__ 출력 : ", __name__)

def hello2py() :
    print("2.py의")

# 코딩하는 문제들 낼 예정, 문제 조금 장담은 못함.
# 
#     