from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
import os
import requests
from tqdm import tqdm

#!!!!!주의 아주아주 야아아아아악간의 사소한 에러가 있을수 있음!!!!!!!

def 폴더생성(st):
    if not os.path.isdir(st):
        os.mkdir(st)
def 파일이름(st):
    for i in "/\\\"?*<>|:":
        st = st.replace(i, "")
    st = st.replace(" ", "_")
    return st

user=input("검색:")

폴더생성("네이버이미지검색")
폴더생성(f"./네이버이미지검색/{user}")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('lang=ko_KR')

dv=webdriver.Chrome(chrome_options=chrome_options)
dv.get(f"https://search.naver.com/search.naver?where=image&sm=tab_jum&query={user}")
last_height = dv.execute_script("return document.body.scrollHeight")

while tqdm(True):
    dv.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(2.5)
    new_height = dv.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

score=dv.page_source

soup=BeautifulSoup(score,"html.parser")
num=0
for i in tqdm(range(10)):
    name=파일이름(soup.select("div > div.thumb > a > img")[i].get("alt"))
    pict=(soup.select("div > div.thumb > a > img")[i].get("src"))
    if not pict.split("/")[0]=="data:image":
        num+=1
        res=requests.get(pict)
        f=open(f"네이버이미지검색/{user}/{name}.png","wb")
        f.write(res.content)
        f.close()
