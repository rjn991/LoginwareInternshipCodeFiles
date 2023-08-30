from ubidots import ApiClient
from tkinter import *
w=Tk()
w.title("Calculator")
w.geometry("1000x600")
w.configure(bg="#F5A0D6")
api=ApiClient(token="BBFF-OHSRRigalIWGRTrTLtYTYxjNCP8v32")
b1=api.get_variable('64eed455861634000b3a9d90')
def click(a):
    print(a)
    b1.save_value({"value":a})

ron=Button(w,text="RED ON",height=4, width=15,command=lambda :click(0))
ron.place(x=30,y=30)

gon=Button(w,text="GREEN ON",height=4, width=15,command=lambda :click(1))
gon.place(x=200,y=30)

bon=Button(w,text="BLUE ON",height=4, width=15,command=lambda :click(2))
bon.place(x=400,y=30)

off=Button(w,text="OFF",height=4, width=15,command=lambda :click(3))
off.place(x=100,y=150)
w.mainloop()
