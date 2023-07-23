import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import requests
from bs4 import BeautifulSoup
import os
from time import sleep

#!!!!!주의 아주아주 야아아아아악간의 사소한 에러가 있을수 있음!!!!!!!

win=tk.Tk()

f=open("pic.jpg","wb")

#배경
img =Image.open('background.jpg')
bg = ImageTk.PhotoImage(img)
back= Label(win, image=bg)
back.pack()
#---
def p():
    #크롤링-----------------
    inp_1=(str(inp.get()))
    res=requests.get(f"https://music.bugs.co.kr/search/integrated?q={inp_1}")
    soup=BeautifulSoup(res.text,"html.parser")
    site=(soup.select_one("#DEFAULT0>table>tbody>tr").get("albumid"))
    res2=requests.get(f"https://music.bugs.co.kr/album/{site}?wl_ref=list_tr_07_search")
    soup2=BeautifulSoup(res2.text,"html.parser")
    

    img2=(soup2.select_one(".big > a > img").get("src"))
    res2=requests.get(img2)
    f=open("pic.jpg","wb")
    f.write(res2.content)

    img3 = ImageTk.PhotoImage(Image.open('pic.jpg'))
    label3 = Label(image=img3)
    label3.image=img3

    artist=Label(win,width=30,borderwidth= 3,relief="sunken",background = "#3d9ee5",text=("아티스트:",soup2.select_one("tbody > tr:nth-child(1) > td > a").text.strip()))
    musucname=Label(win,width=30,borderwidth= 3,relief="sunken",background = "#3d9ee5",text=("노래이름:",soup2.select_one(".innerContainer>h1").text.strip()))
    datetime=Label(win,width=30,borderwidth= 3,relief="sunken",background = "#3d9ee5",text=("발매일:",soup2.select_one("td>time").text.strip())).place(x=345,y=125)
    agency=Label(win,width=30,borderwidth= 3,relief="sunken",background = "#3d9ee5",text=("기획사:",soup2.select_one("table > tbody > tr:nth-child(6) > td").text.strip())).place(x=345,y=165)
    artist.place(x=370,y=33)
    musucname.place(x=20,y=120)
    #----------------------

    label1=Label(win)

win.geometry("800x500")
win.title("apple")
win.resizable(False, False)
inp = Entry(win, width=30)
button = tk.Button(win, text="검색",command=p)

inp.place(x=53,y=32)
button.place(x=270,y=32)

win.mainloop()

f.close()

os.remove("pic.jpg")