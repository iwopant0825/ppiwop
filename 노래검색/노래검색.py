import requests
from bs4 import BeautifulSoup
from time import sleep
import os
print()
inp=input("노래검색:")

#!!!!!주의 아주아주 야아아아아악간의 사소한 에러가 있을수 있음!!!!!!!

res=requests.get(f"https://music.bugs.co.kr/search/integrated?q={inp}")
soup=BeautifulSoup(res.text,"html.parser")
site=(soup.select_one("#DEFAULT0>table>tbody>tr").get("albumid"))
res2=requests.get(f"https://music.bugs.co.kr/album/{site}?wl_ref=list_tr_07_search")
soup2=BeautifulSoup(res2.text,"html.parser")

print()
print("아티스트:",soup2.select_one("tbody > tr:nth-child(1) > td > a").text.strip())
print("노래이름::",soup2.select_one(".innerContainer>h1").text.strip())
print("발매일:",soup2.select_one("td>time").text.strip())
print("기획사:",soup2.select_one("table > tbody > tr:nth-child(6) > td").text.strip())
img2=(soup2.select_one(".big > a > img").get("src"))
res2=requests.get(img2)
f=open("pic.png","wb")
f.write(res2.content)
f.close()
sleep(2)

os.remove("pic.png")
