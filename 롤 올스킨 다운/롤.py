from bs4 import BeautifulSoup
import requests
import os
from tqdm import tqdm

def file(st):
    if not os.path.isdir(st):
        os.mkdir(st)

def 사용불가(no):
    for i in "/\\\"?:*<>|":
        no=no.replace(i,"")
    return no

file("롤 스킨")

for i in tqdm(range(1,163)):
    res=requests.get(f"https://lol.inven.co.kr/dataninfo/champion/detail.php?code={i}")
    soup=BeautifulSoup(res.text,"html.parser")
    name=(soup.select_one(".korName").text.strip())
    file(f"롤 스킨/{name}")
    s=0
    for i2 in range(len(soup.select(".askin>img"))*2):
        sname=(soup.select(".askinname")[i2].text.split("-"))
        if not sname[1]==' 게임내 이미지':
            f=open(f"롤 스킨/{name}/{(사용불가(sname[0].strip()))}.png","wb")
            sp=(soup.select(".askin>img")[s].get("src"))
            r=requests.get(sp)
            f.write(r.content)
            s+=1
            






