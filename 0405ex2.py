import random

# print(random.randint(0,10))
'''
from random import randint #ranint 를 사용하기 위해서 파이썬이 이걸 보고 파악한다.
from random2 import randint

print(random.randint(0,10000))
'''
#놀이동산 탑승 문제

# 총 정원 4명

#정원이 차면, 놀이기구 시작
#조건 키 150 이상만 탈 수 있음,
#사람들한테 키를 물어보고, 탑승시키시오.
#150이상 4명이 되면, 놀이기구 시작
'''
pusedo code
   while True :
      키를 물어본다. -> 키를 입력받는다.
      if 키 -> 150 이상이면
          놀이기구 탑승하세요 출력
          카운트 + 1
      elif 카운트가 4가 되면
          놀이기구가 시작합니다.
          break
      
      else 키 -> 150 이하면
        이 놀이기구는 150이상만 탑승할 수 있습니다. 출력

'''    



count = 0
while True:
    height = input("손님 키가 어떻게 되십니까?")
    if int(height) >= 150 :
        print("놀이기구 탑승이 가능합니다!")
        count += 1
        print("놀이기구 탑승 인원 :",count,"명")
        if count == 4 :
           print("놀이기구가 시작됩니다!")
           break
    else:
        print("죄송합니다. 이 놀이기구는 150 이상만 탑승 가능합니다.")  
        continue      
