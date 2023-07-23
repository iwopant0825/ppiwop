from tkinter import *
from random import randint as ri
from PIL import ImageTk
from bs4 import BeautifulSoup
import requests
import os
from random import randint
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep

win=Tk()
win.geometry("1000x500")

mainframe=Frame(win)
lac=Frame(win)

def click():
    t=Label(lac,text=(title[i]).text,font=("맑은고딕", 20, "bold")).pack()
    n=Label(lac,text=soup.select_one("#courses_section > div > div > div > main > div.courses_container > div > div:nth-child(1) > div > a > div.card-content > div.instructor").text,font=("맑은고딕", 20, "bold")).pack()
    r=Label(lac,text=soup.select_one("#courses_section > div > div > div > main > div.courses_container > div > div:nth-child(1) > div > a > div.card-content > div.rating > span").text,font=("맑은고딕", 20, "bold")).pack()
    m=Label(lac,text=soup.select_one("#courses_section > div > div > div > main > div.courses_container > div > div:nth-child(1) > div > a > div.card-content > div.price").text,font=("맑은고딕", 20, "bold")).pack()
    mainframe.pack_forget()
    lac.pack()

res=requests.get("https://www.inflearn.com/courses?charge=free&order=popular")
soup=BeautifulSoup(res.text,"html.parser")
title=soup.select("div.card-content > div.course_title")
buttons=[None]*10

for i in range(10):
    buttons[i]=Button(mainframe,text=(title[i]).text,font=("맑은고딕", 20, "bold"),command=click)
    buttons[i].pack()

mainframe.pack()
win.mainloop()