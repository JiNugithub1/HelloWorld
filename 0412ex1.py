#0412 python


#자료형 -> 리스트, 튜플, 딕셔너리, 집합
#리스트는 추가, 삭제가 자유롭지만 튜플은 자유롭지 못하다.

#리스트 => ["김밥","떡볶이","돈까스"] 튜플 => ("김밥","떡볶이","돈까스") 딕셔너리 => {key 1 : value 1, key 2 : value 2 ...}
'''
adress = {"jinwoo": 'Gm',"faker" : 'Seoul'}
'''

lst =  []

lst.append("chicken")
lst.append("pizza")
lst.append("coke")
lst.append("kimchi")
lst.append("washabi")
lst.append("hambuger")
lst.append("kimbap")
lst.append("bulgogi")
lst.insert(0,"sandwich") #append는 기존 리스트에 'value' 값 뒤에 추가, insert는 원하는 위치에 새 'value'값을 집어 넣는 것.
lst.insert(1,"saushi")


'''
print("list에서 3번째 있는 값입니다. -> ",lst[2])

#for 첫 번째 출력하는 법
for i in range(len(lst)) :
    print(lst[i])


#for 두 번째로 출력하는 법
for i in lst :
    print(i)
                 
print(lst)
print(lst.count("pizza"),lst.index("pizza"))

'''

# slicing

# lst[start:end:step]

# lst[0,10,1] 0~(10-1),step 수 만큼 뛰어 넘어라.

lst[::]
lst[:len(lst):1]
# 둘이 같은 뜻이다. 어떻게 사용하든 상관없다.


'''
print(lst[0:len(lst):1])
print(lst[0:8:2]) # 0~7 2칸씩 뛰어넘기
print(lst[3:7:1]) # 3~6
print(lst[::-1]) # 거꾸로
print(lst[0:6:3]) # 0~5, 3칸씩 0,3 
'''
'''
lst.append("pizza")
lst.append("pizza")
print(lst)
lst.remove("pizza")
print(lst)

lst.remove("pizza")
print(lst)

lst.remove("pizza")
print(lst)

lst.append("coffee")
print(lst)

item1 = "coffee"
if item1 in lst :
    lst.remove(item1)
    print("coffee exit in lst",lst)
else:
    print("coffee NOT exit in lst",lst) 
'''

'''
# pop
print(lst)
print("lst.pop(#제일 마지막 값= 최근 값) : ",lst.pop())
print(lst)   

print("lst.pop() : ",lst.pop())
print(lst)

print("lst.pop(0) : ",lst.pop(0))
print(lst)
'''


#list 1 + list 2
'''
print(lst)
dessert = ["케잌","커피","우유","와플"]
print(dessert)
lst.extend(dessert)

print(lst)

x="15"

print(type(x))

print(x+"1") # "15" + "1" = "16"\(x) "15" + "1" = 151\(O)
#print(x+1)
print(int(x)+1) # 15 + 1 = 16 )\(o)
print(type(x))
'''
# sort()
l1 = ['orange','apple','pineapple','mango','blueberry','banana','kiwi']

# sorted(l1) # basic python function
# l1.sort() # list method

#print(l1)
#print(sorted(l1))
# print(l1)

print(l1)
print("===l1.sort() execute===")
l1.sort()
print(l1)

l1.reverse()
print(l1)

l1.clear() #비어있다.
print(l1)

'''
del l1
print(l1) # 'NameError: name 'l1' is not defined' 오류가 난다.
'''

# 리스트 컴프리핸션
# 리스트를 선언할 때, 짧게, 빠르게 간결하게 하고 싶다.
'''
#0~10까지 숫자가 있는 리스트를 선언하라.
#)1 
l2 = [0,1,2,3,4,5,6,7,8,9,10]
print(l2)


#)2 for 문으로 append
l3 = []
for i in range(11) : # 0~10 
    l3.append(i)
print(l3)

#)3 리스트 컴프리핸션 for문마저 귀찮다...!
l4 = [i for i in range(11)]
print("l4 : ",l4)

#4) 0~10 까지의 숫자의 제곱을 리스트에 넣어라
#[0,1,4,8,...,81,100] i**2


l5 = [i**2 for i in range(11)]
print("l5 : ",l5)


#)5 0-10 까지의 숫자의 3배수 리스트에 넣어라
l6 = [i*3 for i in range(11)]
print("l6 : ",l6)

#)6 hello를 10번 넣어라.

l7 = ["hello" for i in range(10)]
print("l7 : ",l7)

#)7 0-10까지 짝수들의 제곱을 리스트에 넣으시오.

l8 = []
for i in range(11) :
    if(i%2==0) :
        if(i%3==0) :
          l8.append(i**2)

print("짝수들의 제곱 : ",l8)

l80 = [i**2 for i in range(11) if i%2==0 if i%3==0]

print(l80)

'''


#list 를 복사
a = [0,4,16,36, 64, 100]
b = a #Memory adress 공유
print("a : ",a)
print("b : ",b)

a.pop()
print("------------------after pop()------------------")
print("a : ",a)
print("b : ",b)

print(a is b) # True를 출력한다. 같은 메모리를 참조한다고 생각하면 된다.
b.append("333")
print("after b.append('333')")
print("a : ",a)
print("b : ",b)

#Deep Copy
#)1 c = a[:] #a[:] a에 있는 모든 value를 다 가지고 있다.
#)2 c =a.copy() #deep copy 하기 위한 명령어
#)3 
c  =list(a)

print(a is c) # False 출력. 그 이유는 아예 다른 메모리를 가지기 때문이다.

print("a :", a)
print("c : ",c)

a.pop()
print("after pop()!!!")
print("a : ",a)
print("c : ",c)

c.append("55555")
print("after c.append('55555')")
print("a : ",a)
print("b : ",b)
print("c : ",c)