#0419
# **전에 했던 내용 복습과정

'''
# List
l1 = [1,2,3,4]
t1 = (1,2,3,4,5,6,7,8,9,2,2,2,2,2)
print(l1.count(2))
print(t1.count(2))

# 커피숍 프로그램

menu = ("아메","라떼","유자차")
# 아이스티 추가

# menu1 = ("아메","라떼","유자차","아이스티")
# 하나씩 만들어야 되기 때문에 매우 복잡하다.

menu1 = list(menu)
print(menu1)
menu1.append("아이스티")
print(menu1)
menu = tuple(menu1)
print(menu)


t2 = ()
print(t2)
t3 = 10,20,30,40,50,100,2,6,8 # 괄호가 없어도 튜플로 인식한다.
print(t3) 
i4 = 10
t4 = 10, # 뒤에  ,를 찍으면 튜플로 인식한다.
print(type(i4))
print(type(t4))


lst = [3,4,2,8,6,9,1,10,100]
lst.sort()

print(sorted(t3))
print(t3)

t10 = 1,2,3,4
for i in 1,2,3,4,5 :
    print(i)

'''

# dictionary
'''
# d1 = { k1:v1,k2:v2,k3:v3,k4:v4} # key 값은 중복되면 안돼!
d1 = {}
d2 = dict()

# 사전에 값을 추가하자.
#1) 추가 방법 1
''
student = {}
student[101] = "홍"
student[102] = "김"
student[103] = "박"
print(student)
print("student[101] : ",student[101])
print("student[102] : ",student[102])
print("student[103] : ",student[103])
# error) print("student[0] : ",student['sdds'])
# error )print("student[8] : ",student[0])

lec = { }
lec ['강좌명'] = '파이썬'
lec ['개설년도'] = '2023'
lec ['수강생'] = ['전진우','유지현','강태현']
lec ['수강인원'] = 35
print(lec)


# 인원수를 변경하는 방법

lec['수강인원'] = 20
print(lec)

lec.update({'수강인원':10})
print(lec)

lec.update({'강의실':213,'교수':'이희진'})
print(lec)

#1) 1월부터 12월까지
month = {'k1':'a월','k2':'b월','k3':'c월','k4':'d월','k5':'e월','k6':'f월','k7':'g월','k8':'h월','k9':'i월','k10':'j월','k11':'k월','k12':'l월'}
'''
'''
for key in range(1,13):
    print(month[key])

#2) 2번째 방법
print('#2')
for key in 1,2,3,4,5,6,7,8,9,10,11,12 :
    print(month[key])
'''
# print(month.keys())
# rint(month.values())
# print(month.items())
'''
print(month.keys())
print('#3')
for k in month.keys() : # [k1,k2,k3,k4,e,f ... ,12]
    print(month[k])

print('#4')
#month.valuse()
for v in month.values() : #[1월,2월,3월,4월 ---]
    print(v)

print(month.items())
print('#5')
#month.items()
for h in month.items() : #[(k1:1월),(k2:2월),(k3:3월),(k4:4월) ---]
    print(h)

print('#6')
#month.items()
for item in month.items() :
    # item - > (k1,v1) -> 2차원배열이랑 비슷하다.
    # print("key:",item[0])
    print("value:",item[1])
    # print("  ")
#key xxx
#value xxx

for hoho in month :
    print(hoho)

print(month['k1'])
print(month.get('k1'))
print(month.get('key100'))
# print(month['key100'])

# dictionary

print(month)

print("month.pop('k1') : ",month.pop('k1')) #key값을 줘야함
print(month)
print("month.popitem() : ",month.popitem()) # 맨 마지막 값을 삭제
print(month)
'''

#zip(), enumerate()
'''
l1 = ['한식'         ,'중식'     , '일식']
l2 = ['전주식당','전가복','초밥집']
l3 = ['제육',    '탕수육', '연어덮밥',]

z = zip(l1,l2,l3)
print(type(z))
print(z)
print(list(z)) # -> [('한식', '전주식당', '제육'), ('중식', '전가복', '탕수육')] 개수가 적은 튜플들을 만들어준다.

#dictionary
# list = > dictionary x
#l2 => zl, l3 -> value

z1 = zip(l2,l3)
print(dict(z1))
#print(list(z1))

#z2 = zip(l1,l2,l3)
#print(dict(z2)) # Error Message -> dictionary update sequence element #0 has length 3; 2 is required

z2 = zip(l1,zip(l2,l3))
print(dict(z2))

# 1개 리스트를 dictionary 로 변경
#     0         1           2
l4 = ['제육',        '탕수육',       '연어덮밥']

print(enumerate(l4)) # -> <enumerate object at 0x00000262A90E7830> 메모리 값
print(list(enumerate(l4)))
print(dict(enumerate(l4)))

'''



#문제
#과목을 주면 강의실을 알려주는 시스템

subject = ['파이썬','자바','C++','AI','알고리즘']
classroom = [101,102,103,104,105]
# 1) dictionary로 변환해서 활용
# 2) 무한루프로 강의실을 알려줘라
# 3) quit 이라는 단어가 들어오면, 강의실 알려주는 시스템을 종료해라
# 4) ekfms rhkahrdmf anfdjqhaus, "몰라요" 다시 과목명 물어보는 것으로 돌아간다.
# 5) continue, break 활용할 것

z1 = zip(subject,classroom)
dic1 = dict(z1)

while True :
        subserch = input("과목명을 입력하세요");
        if(subserch == "quit") :
            print("종료합니다...")
            break
        if subserch in dic1.keys() :
            print("강의실은 ", dic1[subserch])
            continue
        else :
            print("몰라용")
            continue
                    
