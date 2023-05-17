#0517

from bs4 import BeautifulSoup 
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Key
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
'''
import requests


headers = {
    "User-Agent" : "DongYang Jinwoo"
}



#------------------------------------------------------------------------------------------------------------------------
webpage = requests.get("https://n.news.naver.com/article/006/0000118094?cds=news_media_pc&type=editn",headers=headers)
# requests를 요청할 때 header에 보냄.

#print(webpage)
#print(webpage.content)
soup=BeautifulSoup(webpage.content, "html.parser")
#print(soup)

#news = soup.select_one("#dic_area").get_text().strip()

#print(news)

#------------------------------------------------------------------------------------------------------------------------
webpage2 = requests.get("https://n.news.naver.com/article/006/0000117871?sid=101",headers=headers)
soup2 = BeautifulSoup(webpage2.content, "html.parser")

news2 = soup2.select_one("#dic_area").get_text().strip()

print(news2)
