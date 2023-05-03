#0503

#함수

'''
함수 이름 -> addtree
기능 : 3을 더함.
input : 숫자 1개
output : 숫자 1개, input 숫자에다가 3을 더한 것을 내보냄

'''
'''
def function_name(input1,input2,input3) :
    #수행문 1
    #수행문 2

'''

#1
def addtree(num) :
    num = num+3
    return num

'''
result = addtree(100)
print(addtree(100))
print(result) # result = 103



# printaddtree(100) NameError: name 'printaddtree' is not defined <- 에러출력(사유 : 함수를 정의하지 않았기 때문)
#2
def printaddtree(num) : # print를 함수 내에서 선언하여 함수를 호출하면 바로 값을 확인할 수 있다.
    print(num +3)

printaddtree(100)

#-------------------------------------------------------------------------

'''
# 주의사항으로는 함수를 호출하고, 함수를 불러와야 한다.

# function 1호출
# function 이름 - hello

# parameter - name 1, name 2
# 결과 print(hello name 1, hello name2)


# )1 값을 초기화 해서 줄 수도 있다.
'''
def hello(name1="jinwoo",name2="max") :
    print("hello",name1)
    print("hello",name2)

# hello()
'''

def hello(name1,name2) :
    print("hello",name1)
    print("hello",name2)

hello("Jeon","Max")    

# function 2 호출
# parameter - num1, num2
# 결과 - return num1 + num2
# mysum

def mysum(num1,num2):
    return num1+num2

result = mysum(100,200)    

# 2
def hello(name1="jinwoo",name2="max") :
    print("hello",name1)
    print("hello",name2)



print("하")
print(1,2,3,4,5,5)
print(22,2,22,22,22,5)

#--------------------------------------------------------------------------------------
'''
mysum2
인자는 몇개가 들어올지 모름
결과 - 모든 인자의 합을 return

'''

def mysum2(*numbers) :
    result = 0
    for num in numbers :
        result = result+num
    
    return result     

print(mysum2(1,2,3,4,55,67,89,22))
print(mysum2(1,1,1,1,1,1,1,1,1))



list1 = [10,10,10,10,10]
list2 = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]

print(mysum2(*list1))
print(mysum2(*list2))

#------------------------------------------------------------------------------------
'''
key,value pair

cafe function

메뉴 = 가격,
출력해주는 function을 만들자.
'''



def cafe(**keyvalue):
    for key in keyvalue : #아메,라떼,핫초코
        print(key," ",keyvalue[key]) # 아메, 2000
 

cafe(Americano=2000,Latte=3000,Hotchoco=4000)
print("==============")
cafe(Americano=200,Latte=3000)
print("==============")
cafe(Americano=200)


menu = {'아메리카노':1000,'카푸치노':2000,'카페모카':2500,'에스프레소':3000}



cafe(**menu)
print("DM으로 문의해주세요 ☞ ☜")

print("-------------------------------------------------")
#-----------------------------------------------------------------------------------------------
######################################
# Lambda function
# 짧게 간결하게 쓰고 싶어서 개발된 function
# function 이름 짓기 싫다.
# 수행문이 한줄이다.


'''
def addtree(num) :
    num = num+3
    return num

addtree(110)

(lambda num : num +3)(100)

print(addtree(100))
print((lambda num : num +3)(100))
'''


#--------------------------------------------------------------------------------------------------


#1) 숫자를 입력받아서, 10을 곱해서 return 함수 - lambda로 만들어라.
#)2 숫자를 두개 입력, 두개를 곱해서 return - lambda
    #호출까지

#) answer

def num3(num) :
    return num*10

print(num3(20))
print((lambda num3 : num3*10)(20))

#)2 숫자를 두개 입력, 두개를 곱해서 return - lambda
    #호출까지
def num4(n1,n2) :
    return n1*n2

print(num4(3,5))    

print((lambda n1,n2 : n1*n2)(3,5))

#-----------------------------------------------------------------------------------------------------------------------


# map() 함수
'''
map(function, list)
map(function,[1,2,3,4,5])
map(function,[1,2,3,4,5])
[function(1), function(2), ... ,function(5)]
'''

print(list(map(addtree,[10,20,30,40,50]))) # output : [13, 23, 33, 43, 53]
print(list(map(lambda x : x +3,[10,20,30,40,50]))) # output : [13, 23, 33, 43, 53]
# -> lambda함수를 써도 똑같이 나온다. 그 이유는 addtree() 함수와 lambda가 같기 때문이다.

#-----------------------------------------------------------------------------------------

lst = [1,2,3,4,5]
# 5배를 하고,10을 더해서 결과를 list로 출력하시오.

#1) function
def a1(num) :
    return num*5 +10
print(list(map(a1,lst)))    

#2) lambda
print(list(map((lambda x : x*5+10),lst)))


# 두개의 list를 하나씩 뽑아서, 두개를 더해서 하나의 리스트로 만들어라
# 결과값 [11,22,33,44,55]

lst1=[10,20,30,40,50]
lst2=[1,2,3,4,5]

#1) function
def b1(x,y):
    return x+y

# map(function,입력 리스트)

print(list(map(b1,lst1,lst2))) # [11, 22, 33, 44, 55]
# [b1(10,1),b1(20,2),...,b1(50,5)]


#2) lambda

print(list(map(lambda x,y : x+y,lst1,lst2))) # [11, 22, 33, 44, 55]

#=================================================================================================

#filter(ex)양수인가? 음수인가?)
# 조건을 만족하는가? 만족하면 결과물에 포함, 만족하지 않으면 포함 X
# map이랑 마찬가지로, 입력 리스트로 받아서, 그걸 결과로 나타냄


#ex) filter(function,list)

def filterfnc(num) :
    if num > 0 :
        return True
    else :
        return False        


print(list(filter(filterfnc,[10,-3,-9,8,50,-1])))        

# 조건문을 가진경우 filter()를 이용해서 참의 결과와 거짓의 결과를 도출할 수 있다.
# lambda 표현 가능

print(list(filter(lambda x : x>0,[10,-3,-9,8,50,-1])))


def is_even(x) :
    if x % 2 == 0:
        return True
    return False

# for 반복문 이용
arr1 =[]
for val in range(1,11) :
    if is_even(val):
        arr1.append(val)
print(f"arr function : {arr1}") 


#filter 함수 이용
arr2 = list(filter(is_even,range(1,11)))
print(f'arr filter : {arr2}')