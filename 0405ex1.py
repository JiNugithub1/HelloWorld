#0405
#String

# str = "자바수업 파이썬수업 파이썬수업 파이썬수업 파이썬수업 파이썬수업 파이썬수업 파이썬수업 파이썬수업 파이썬수업 파이썬수업"
str2 = "자바수업,파이썬수업,파이썬수업,파이썬수업,파이썬수업,파이썬수업,파이썬수업,파이썬수업,파이썬수업,파이썬수업,파이썬수업"


# format
# 3+4 = 7
# print(3,"+",4,"=",3+4)
f = "{} + {} = {}".format(3,4,7)
f2 = "{0} + {1} = {2}, {2}, {2}, {2}".format(3,4,3+4) # 순서를 이용해서 값을 대입할 수 있다.
f3 = "{0:d} + {1:f} = {2:f}, {2:f}, {2:f}, {2:f}".format(3,4.0,3+4.0)
f4 = "{0:10d} + {1:10f} = {2:10f}, {2:0.4f}, {2:10.3f}, {2:f}".format(3,4.0,3+4.0)

'''
print(f2) # format 함수로 사용할 수 있음!
print(f3)
print(f4)
'''

#join
# print("**".join(str))

'''
#replace(바꾸고 싶은 단어 , 바꾼 단어,몇개만 바꿀건지)
print(str.replace("파이썬","자바",3))

#count
print(str.count("파이썬")) # -> 숫자 10 출력

#find, index
print("find :",str.find("업")," index :" ,str.index("업"))
print(str.find("AI")) # 없는 단어를 찾아달라고 하면 -1 -> return
print(str.index("AI")) # index는 오류를 출력한다. 'ValueError: substring not found' -> return
'''

'''
# split
print(str.split())
print(str2.split(","))
print(str2.split("업"))
'''
'''
#bool
print(type(True),type(False))
a = 'hello'
print(bool(a),bool("hi"),bool(3),bool(1.2),bool(-2)) # bool형은 True와 False문 밖에 존재 하지 않는다.
print(bool(0),bool(""))

print(int(True),int(False), str(True))
'''

# if(조건문)

# 구조
#if 조건1 : 
    #실행문1 -> 참
#else :
    #실행문2 -> 거짓

#오전/오후
'''
h = 20
#h가 12보다 작을 때
if h < 12 :
   print("오전", h,"시가 12보다 작다.")

#12 < h < 18
elif h < 18 :
    print("오후",h,"가 12보다 크고 18보다 작다.")   

#h가 12보다 클 때
else :
    print("저녁",h,"시가 18보다 크다.")
'''

# 학식 먹을래/ if문을 사용한다
'''
a = input("밥 먹을래?")

if a == "yes" :
    print("학식 먹을래?")
    a= input()
    if a == "yes" :
        print("8호관 3층에 있어!")
    
    else  :
        print("Subway 어때?")
        cafeteria = input()
       
        if cafeteria == "yes" :
            print("8호관 1층에 있어!")
        else :
            print("꺼져")         
else :
     print("꺼져")         
'''

# for문과 while문

# in range

#for i in 10,25,32,45345,2332,555 : 
     #print("i :",i)
#for i in range(0,20,1):
    # print("i : ",i)     

#for i in range(20) :
    # print("i :",i)

#for i in range(3,21,3) :
    #print("i :" ,i)     
'''
sum =0
for i in 1,2,3,4,5,6,7,8,9,10 :
    #sum = sum + i
    sum += i
    print(i," 번째 loop입니다. sum은 ",sum," 입니다.")
    #print("하하하하하하")
'''     
'''
print("range를 사용하였음!")
sum =0
for i in range(1,11,1) :
   # sum = sum + i
   sum += i

   print(i," 번째 loop입니다. sum은 ",sum," 입니다.")
    #print("하하하하하하")
else:
    print("for문이 정상종료 하였습니다.")  

print("else밖의 문구 : for문 종료")    
'''
# while

#0부터 10까지 숫자를 찍음
'''
sum =0
n=0
while(n<11) :
    sum += n
    print(n,"번째 sum = ",sum)
    n += 1 

print("while 밖에서 sum의 값 :",sum)   

while False :
    print("no")
while 0:
    print("실행이 되지 않음")

 

#while 0:
    #print("실행이 되지 않음")

#while True :
    #print("infinity loop")
'''

#break continue
# 단어 입력을 무한 루프로 받는다.
# 그 글자를 3번 써줌
#'exit' -> 루프를 끝내고 종료
#'apple' -> 3번 안쓰고 그냥 다시 단어 입력을 받음.

'''
while True :
      word = input("단어를 입력하세요..")
      if word == "exit" :
            print("넌 exit 를 입력했다.. break를 만날꺼야!")
            break
            print("break 뒤에 문장")
      elif word == "apple":
            print("넌 apple을 입력했다.. continue를 만난다")
            continue
            print("continue 뒤의 문장")
      else:
            for i in range(3):
                 print(word,end=" ")
                 print("해당 단어 끝!")

      print("apple을 넣으면 이걸 절대 볼 수 없음!")                 
                 
'''

