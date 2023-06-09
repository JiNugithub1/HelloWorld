#0510

# Moduels
# 모듈을 불러오는 다양한 import 구문
# 직접 모듈 생성과 사용

# 모듈을 이용할 수 있는 것이 중요함.


# 함수나 변수의 파이썬 코드가 저장된 소스 모듈
# import(써드 파티 모듈)
# numpy, pandas, ...
#----------------------------------------------------------------------------------------------------
'''
import random # 랜덤 난수 모듈

print("random.randint(10,100)",random.randint(10,100))

import math # 수학 모듈 
print("math.fsum([1,1,1,1,1,1,1,])",math.fsum([1,1,1,1,1,1,1,]))




import math as m # as를 통해 키워드로 만들 수 있다.
print(m.fsum([1,1,1,1,1,1,1,]))
print(m.pow(10,3)) # 10^3


# pow(10,3) M없이 그냥 POW만 사용하고 싶다. 그럴 땐
from math import pow as p # from을 이용해서 만들 수 있다.
print(p(10,3)) # print(m.pow(10,3)) # 10^3와 값이 똑같이 나오는 것을 알 수 있다.
'''
#----------------------------------------------------------------------------------------------------

# import문에 간단한 예제

#0510.py
#김길동
import ya

print("=================")
ya.helloya()

print("___name in 0510.py :",__name__)

from moduley.data import yaa as selected

selected.helloyaa()





#------------------------------------------------------------------------------------------------------




