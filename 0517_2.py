#0517 (2) Chrome 데이터 환경 구축
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service


from webdriver_manager.chrome import ChromeDriverManager

service = Service(executable_path=ChromeDriverManager().install())
driver=webdriver.Chrome(service=service)

'''
#(1) news를 가져온다

driver.get("https://www.naver.com/")
time.sleep(3)

#(2)원하는 버튼을 누르는 명령을 한다. 뉴스 버튼 누름
#원하는 주소에 검사를 누르고 우클릭한 뒤 Copy full XPath를 클릭하면 그 주소에 경로를 알 수 있다.
driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[3]/div[1]/div[1]/ul[2]/li[2]/a").click()
time.sleep(3)

newstitle1 = driver.find_element(By.XPATH, "/html/body/div[2]/div/section[1]/div[2]/div/div[1]/div[2]/div[1]/div/div[2]/a/div[2]/div").text
print(newstitle1,"\n")

newstitle2 = driver.find_element(By.XPATH, "/html/body/div[2]/div/section[1]/div[2]/div/div[1]/div[2]/div[1]/div/div[4]/a/div[2]/div").text
print(newstitle2)

#------------------------------------------------------------------------------------------------------------------------------------------
'''
'''
#(3) 아파트 가격 알아보기
driver.get("https://m.land.naver.com/search")
time.sleep(1)

driver.find_element(By.XPATH, "/html/body/div[1]/div/div[10]/div[2]/header/div[2]/form/div/input").click()
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[10]/div[2]/header/div[2]/form/div/input").send_keys("우성꿈동산")
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div[10]/div[2]/header/div[2]/form/div/button[2]/i").click()
time.sleep(1)

#전세값 가져오기
rentprice = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[5]/div/section/div/div/div[1]/div[2]/div/div/dl[2]/dt").text
print(rentprice)
'''


#또 다른 아파트 전세값 가져오기
'''
driver.get("https://m.land.naver.com/search")
time.sleep(1)

driver.find_element(By.XPATH, "/html/body/div[1]/div/div[10]/div[2]/header/div[2]/form/div/input").click()
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[10]/div[2]/header/div[2]/form/div/input").send_keys("대치동 동민맥스빌(A동,주상복합)")
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div[10]/div[2]/header/div[2]/form/div/button[2]/i").click()
time.sleep(1)

rentprice = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[5]/div/section/div/div/div[1]/div[2]/div/div/dl[2]/dd").text
print(rentprice)
#-----------------------------------------------------------------------------------------------------------------------------------
'''
# 주식 증권 알아보기

driver.get("https://finance.naver.com/")

subject1 = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[1]/th/a").text
subject2 = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[2]/th/a").text
subject3 = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[3]/th/a").text


print(subject1,subject2,subject3)

lst = []
for i in range(10) :
    subject = driver.find_element(By.XPATH, f"/html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[{i+1}]/th/a").text
    lst.append(subject)

print(lst)   

lst2 = []
dic = {}
for i in range(10) :
    subjects = driver.find_element(By.XPATH, f"/html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[{i+1}]/td[{i+1}]").text
    lst2.append(subjects)
    dic.keys(i)
