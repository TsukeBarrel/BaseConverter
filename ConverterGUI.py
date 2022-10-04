#!/usr/bin/env python
# coding: utf-8

# In[7]:


#コンバーターGUIパーツ

from tkinter import *
from tkinter import ttk
import ConverterMainbody as CM

win = Tk()
win.title("進数間変換器")
win.geometry("480x360")
win.config(background = "Light Gray")
win.grid_rowconfigure(0, weight = 1)
win.grid_columnconfigure(0, weight = 1)

frame1 = Frame(win)
frame2 = Frame(win)

result1 = StringVar()
result2 = StringVar()
Tag1 = StringVar()
Tag2 = StringVar()
Tag3 = StringVar()
BaseRes1 = StringVar()
BaseRes2 = StringVar()

def Change_Win(frame_num):
    frame_num.tkraise()
    
def Set_Result(selection, input_value):    
    Tmp1 = ""
    Tmp2 = ""
    Tmp1, Tmp2 = CM.main(selection, input_value)
    result1.set(Tmp1)
    result2.set(Tmp2)
    BaseRes1.set(str(Tag1.get()) + " : " + str(result1.get()))
    BaseRes2.set(str(Tag2.get()) + " : " + str(result2.get()))


def FrontPage():
        
    selection = StringVar()
    choice = ["2進数", "10進数", "16進数"]
    Tgt = ["10進数", "16進数"]

    def selected(event):
        select = cb.get()
        Tgt = []
        Tgt = [i for i in choice if not i == select]
        Tmp1, Tmp2 = Tgt
        Tag1.set(Tmp1)
        Tag2.set(Tmp2)
        Tag3.set("変換元 : " + str(cb.get()))
    
    cb = ttk.Combobox(frame1, state = "readonly", textvariable = selection, values = choice, font = ("Meiryo", "15"))
    cb.set(choice[0])
    cb.bind("<<ComboboxSelected>>", selected)
    label1 = Label(frame1, text = "1. 変換元の進数を選んでください", font = ("Meiryo"))
    button1 = Button(frame1, text = "決定", command = lambda: [Change_Win(frame2), Set_Result(cb.get(), input_value.get())], font = ("Meiryo", "10", "bold"))
    button2 = Button(frame1, text = "終了", command = win.destroy, font = ("Meiryo", "10"))
    
    label3 = Label(frame1, text = "2. 変換する数値を入力してください", font = ("Meiryo"))
    input_value = Entry(frame1, justify = "center", font = ("Meiryo"))

    frame1.grid(row = 0, column = 0, sticky = "nsew")
    label1.pack(padx = 10, pady = 10)
    cb.pack(padx = 10, pady = 10)
    label3.pack(padx = 10, pady = 10)
    input_value.pack(padx = 10, pady = 10)
    button2.pack(side = RIGHT, padx = 10, pady = 10)
    button1.pack(side = RIGHT, padx = 10, pady = 10)
    

    
def Show_Result():
    
    label5 = Label(frame2, text = "結果表示", font = ("Meiryo"))
    label_result1 = Label(frame2, textvariable = BaseRes1, font = ("Meiryo"))
    label_result2 = Label(frame2, textvariable = BaseRes2, font = ("Meiryo"))
    label3 = Label(frame2, textvariable = Tag3, font = ("Meiryo"))
    button5 = Button(frame2, text = "終了", command = win.destroy, font = ("Meiryo", "10", "bold"))
    button6 = Button(frame2, text = "戻る", command = lambda: Change_Win(frame1), font = ("Meiryo", "10"))
    
    frame2.grid(row = 0, column = 0, sticky = "nsew")
    label5.pack(padx = 10, pady = 10)
    label3.pack(padx = 10, pady = 10)
    label_result1.pack(padx = 10, pady = 10)
    label_result2.pack(padx = 10, pady = 10)
    button6.pack(side = RIGHT, padx = 10, pady = 10)
    button5.pack(side = RIGHT, padx = 10, pady = 10)
    
    
    
FrontPage()
Show_Result()
Change_Win(frame1)
win.mainloop()

