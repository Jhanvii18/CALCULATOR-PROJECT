def ba(number):
    e.insert(END,number)
def clear():
    e.delete(0,END)
def equal():
    equation = e.get()
    result = eval(equation)
    e.delete(0, END)
    e.insert(END, result)


from tkinter import *
a=Tk();
a.title("Simple Calculator")
a.geometry('390x550')
e=Entry(a,text=" ",width=60,borderwidth=5)
e.grid(row=0,column=0,columnspan=6)
b1=Button(a,text="1",padx=40,pady=40,command=lambda:ba(1)).grid(row=1,column=0)
b2=Button(a,text="2",padx=40,pady=40,command=lambda:ba(2)).grid(row=1,column=1)
b3=Button(a,text="3",padx=40,pady=40,command=lambda:ba(3)).grid(row=1,column=2)
b4=Button(a,text="4",padx=40,pady=40,command=lambda:ba(4)).grid(row=2,column=0)
b5=Button(a,text="5",padx=40,pady=40,command=lambda:ba(5)).grid(row=2,column=1)
b6=Button(a,text="6",padx=40,pady=40,command=lambda:ba(6)).grid(row=2,column=2)
b7=Button(a,text="7",padx=40,pady=40,command=lambda:ba(7)).grid(row=3,column=0)
b8=Button(a,text="8",padx=40,pady=40,command=lambda:ba(8)).grid(row=3,column=1)
b9=Button(a,text="9",padx=40,pady=40,command=lambda:ba(9)).grid(row=3,column=2)
b0=Button(a,text="0",padx=40,pady=40,command=lambda:ba(0)).grid(row=4,column=0)
b11=Button(a,text="+",padx=40,pady=40,command=lambda:ba("+")).grid(row=4,column=1)
b12=Button(a,text="-",padx=40,pady=40,command=lambda:ba("-")).grid(row=4,column=2)
b13=Button(a,text="*",padx=40,pady=40,command=lambda:ba("*")).grid(row=1,column=3)
b14=Button(a,text="/",padx=40,pady=40,command=lambda:ba("/")).grid(row=2,column=3)
b15=Button(a,text="%",padx=40,pady=40,command=lambda:ba("%")).grid(row=3,column=3)
b16=Button(a,text="=",padx=40,pady=40,command = equal).grid(row=4,column=3)
b17=Button(a,text="CLEAR",padx=170,pady=40,command=clear).grid(row=5,column=0,columnspan=4)



    
