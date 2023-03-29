# a='동양미래대학교'
'''
print(a[0]," ",a[1],"...",a[5]) # p y n
print('python'[0],"...",'python'[1],"...","python"[5])
print("동양미래대학교"[4])
print(len(a))
'''
#--------------------------------------------------------------------------------------
'''
school = '동양미래대학교-컴퓨터소프트웨어공학과'
print("school [::] : ",school[::]) # 동양미래대학교-컴퓨터소프트웨어공학과
print("school[0:len(school):2] : ",school[0:len(school):2]) #동미대교
print("school[8:len(shcool):] : ",school[8:len(school):2]) #컴터프웨공과
print("school[8:len(shcool):] : ",school[8:len(school):])#컴퓨터소프트웨어공학과
print("school[:15:4] : ",school[:15:4])#동양미래대학교-컴퓨터소프트웨어 4칸씩
'''
#--------------------------------------------------------------------------------------
'''
print('동양미래대학교'[5:0:-1])
print('동양미래대학교'[-1:-7:-1])

print("hello \n world")
print("hello \t world")
print("hello\b world")
print("hello \v world")
print("hello\nworld")
'''
#--------------------------------------------------------------------------------------
str_a="hahaha"
str_b='hohoho' 
print(type(str_a))
str_a.replace("ha",'ho')
print(str_a.replace("ha",'ho'))
str_a = str_a.replace('ha','ho')
print('str_a:',str_a)
print('str_b:',str_a)


#--------------------------------------------------------------------------------------
str_c='안녕하세요. 파이썬 수업입니다. 파이썬 파이썬 파이썬 파이썬 파이썬 파이썬 파이썬'
print(str_c.replace("파이썬","자바",5))

#6자리 실수를 입력받는다. ex) 222.788
# 출력: 이 실수의 각 자리의 합을 출력한다. 2+2+2+7+8+8 => ??
#input(), int(),  str.replace()

str_a=input("6자리 실수 입력:")
str_a=str_a.replace(".","")

print("sum : ",int(str_a[0]) + int(str_a[1]) + int(str_a[2]) + int(str_a[3]) + int(str_a[4]) + int(str_a[5]))
#--------------------------------------------------------------------------------------