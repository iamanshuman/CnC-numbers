from tkinter import *
import math
root = Tk()
root.title("calculator")

'''entry fields here'''
e = Entry(root, bd =1 , text="enter number here", bg="grey", fg= "white", cursor= "tcross", exportselection=0)
e.grid(row=0, column=0, columnspan=4 , padx=5, pady=20)

'''functions goes here'''

def button_click(to_print):
    take_input = e.get()
    e.delete(0, END)
    e.insert(0, take_input + to_print) 
    return



def button_click_clear():
    e.delete(0, END)


    
def button_click_clearone():
    count = e.get()
    length = len(count)-1
    e.delete(length, END)

  
def evaluate():
    ans = e.get()
    ans = eval(ans)
    e.delete(0, END)
    e.insert(0, ans)


def button_hex():
    num=e.get()
    num=eval(num)
    result= str(hex(num))
    e.delete(0, END)
    e.insert(0, result)

def button_oct():
    num=e.get()
    num=eval(num)
    result= str(oct(num))
    e.delete(0, END)
    e.insert(0, result)


def button_bin():
    num=e.get()
    num=eval(num)
    result= str(bin(num))
    e.delete(0, END)
    e.insert(0, result)

def button_dec():
    num=e.get()
    num=eval(num)
    result= str(int(num))
    e.delete(0, END)
    e.insert(0, result)

def button_perc(event):
    num=e.get()
    num=eval(num)
    result=str(1/100 * num)
    e.delete(0, END)
    e.insert(0, result)



'''functions ends here'''   


'''buttons comes here'''

button0 = Button(root, text="0", height=1, width=1, fg= "white", bg="#ea1e63", bd=1, activebackground= "#ba165a", padx=20, pady=10, command=lambda: button_click('0'))
button1 = Button(root, text="1", height=1, width=1, fg= "white",  bg="#ea1e63", bd=1, activebackground= "#ba165a", padx=20, pady=10, command=lambda: button_click('1'))
button2 = Button(root, text="2", height=1, width=1, fg= "white",  bg="#ea1e63", bd=1, activebackground= "#ba165a", padx=20, pady=10, command=lambda: button_click('2'))  
button3 = Button(root, text="3", height=1, width=1, fg= "white",  bg="#ea1e63", bd=1, activebackground= "#ba165a", padx=20, pady=10, command=lambda: button_click('3')) 
button4 = Button(root, text="4", height=1, width=1, fg= "white",  bg="#ea1e63", bd=1, activebackground= "#ba165a", padx=20, pady=10, command=lambda: button_click('4')) 
button5 = Button(root, text="5", height=1, width=1, fg= "white",  bg="#ea1e63", bd=1, activebackground= "#ba165a", padx=20, pady=10, command=lambda: button_click('5')) 
button6 = Button(root, text="6", height=1, width=1, fg= "white",  bg="#ea1e63", bd=1, activebackground= "#ba165a", padx=20, pady=10, command=lambda: button_click('6')) 
button7 = Button(root, text="7", height=1, width=1, fg= "white",  bg="#ea1e63", bd=1, activebackground= "#ba165a", padx=20, pady=10, command=lambda: button_click('7')) 
button8 = Button(root, text="8", height=1, width=1, fg= "white",  bg="#ea1e63", bd=1, activebackground= "#ba165a", padx=20, pady=10, command=lambda: button_click('8'))
button9 = Button(root, text="9", height=1, width=1, fg= "white",  bg="#ea1e63", bd=1, activebackground= "#ba165a", padx=20, pady=10, command=lambda: button_click('9'))
buttonAC = Button(root, text="AC", height=1, width=1, fg= "white",  bg="#ea1e63", bd=1, activebackground= "#ba165a", padx=20, pady=10, command= button_click_clear)
buttonClr = Button(root, text="Clr", height=1, width=1, fg= "white",  bg="#ea1e63", bd=1, activebackground= "#ba165a", padx=20, pady=10, command= button_click_clearone)
buttondot = Button(root, text=".", height=1, width=1, fg= "white",  bg="#ea1e63", bd=1, activebackground= "#ba165a", padx=20, pady=10, command=lambda: button_click('.'))
button_multiply = Button(root, text="x", height=1, width=1, fg= "white",  bg="#ea1e63", bd=1, activebackground= "#ba165a", padx=20, pady=10, command=lambda: button_click('*'))
button_divide =  Button(root, text="÷", height=1, width=1, fg= "white",  bg="#ea1e63", bd=1, activebackground= "#ba165a", padx=20, pady=10, command=lambda: button_click('/'))
button_percent =  Button(root, text="%", height=1, width=1, fg= "white",  bg="#ea1e63", bd=1, activebackground= "#ba165a", padx=20, pady=10, command=lambda: button_perc('%'))
button_add = Button(root, text="+", height=1, width=1, fg= "white",  bg="#ea1e63", bd=1, activebackground= "#ba165a", padx=20, pady=10, command=lambda: button_click('+'))
button_subtract = Button(root, text="-", height=1, width=1, fg= "white",  bg="#ea1e63", bd=1, activebackground= "#ba165a", padx=20, pady=10, command=lambda: button_click('-'))
buttonEQUAL = Button(root, text="=", height=1, width=1, fg= "white",  bg="#ea1e63", bd=1, activebackground= "#ba165a", padx=20, pady=10, command=evaluate)
buttonA = Button(root, text="A", height=1, width=1, fg= "white",  bg="#ea1e63", bd=1, activebackground= "#ba165a", padx=20, pady=10, command=lambda: button_click('A'))
buttonB = Button(root, text="B", height=1, width=1, fg= "white",  bg="#ea1e63", bd=1, activebackground= "#ba165a", padx=20, pady=10, command=lambda: button_click('B'))
buttonC = Button(root, text="C", height=1, width=1, fg= "white",  bg="#ea1e63", bd=1, activebackground= "#ba165a", padx=20, pady=10, command=lambda: button_click('C'))
buttonD = Button(root, text="D", height=1, width=1, fg= "white",  bg="#ea1e63", bd=1, activebackground= "#ba165a", padx=20, pady=10, command=lambda: button_click('D'))
buttonE = Button(root, text="E", height=1, width=1, fg= "white",  bg="#ea1e63", bd=1, activebackground= "#ba165a", padx=20, pady=10, command=lambda: button_click('E'))
buttonF = Button(root, text="F", height=1, width=1, fg= "white",  bg="#ea1e63", bd=1, activebackground= "#ba165a", padx=20, pady=10, command=lambda: button_click('F'))

button0o = Button(root, text="oct", height=1, width=1, fg= "white",  bg="#ea1e63", bd=1, activebackground= "#ba165a", padx=20, pady=10, command= button_oct)
button0x = Button(root, text="hex", height=1, width=1, fg= "white",  bg="#ea1e63", bd=1, activebackground= "#ba165a", padx=20, pady=10, command= button_hex)
button0b = Button(root, text="bin", height=1, width=1, fg= "white",  bg="#ea1e63", bd=1, activebackground= "#ba165a", padx=20, pady=10, command= button_bin)
button0d = Button(root, text="dec", height=1, width=1, fg= "white",  bg="#ea1e63", bd=1, activebackground= "#ba165a", padx=20, pady=10, command= button_dec)

buttonx = Button(root, text="0x", height=1, width=1, fg= "white", bg="#ea1e63", bd=1, activebackground= "#ba165a", padx=20, pady=10, command= lambda: button_click('0x'))
buttono = Button(root, text="0o", height=1, width=1, fg= "white", bg="#ea1e63", bd=1, activebackground= "#ba165a", padx=20, pady=10, command= lambda: button_click('0o'))
buttonb = Button(root, text="0b", height=1, width=1, fg= "white", bg="#ea1e63", bd=1, activebackground= "#ba165a", padx=20, pady=10, command= lambda: button_click('0b'))

'''buttons ends here'''

''' binding buttons'''

button0o.bind("<Button-1>", button_oct)
button0x.bind("<Button-1>", button_hex)
button0b.bind("<Button-1>", button_bin)
button0d.bind("<Button-1>", button_dec)

''' binding buttons end'''


'''placing the buttons'''
button0.grid(row=7 , column=1 )
button1.grid(row=6 , column=0 )
button2.grid(row=6 , column=1 )  
button3.grid(row=6 , column=2 )
button4.grid(row=5 , column=0 )
button5.grid(row=5 , column=1 )
button6.grid(row=5 , column=2 ) 
button7.grid(row=4 , column=0 )
button8.grid(row=4 , column=1 )
button9.grid(row=4 , column=2 )
buttonAC.grid(row=8 , column=3 )
buttonClr.grid(row=7 , column=3 )
buttondot.grid(row=7 , column=0 )
button_multiply.grid(row=2 , column=3 )
button_add.grid(row=2  , column=0 )
button_divide.grid(row=2 , column=2 )
button_percent.grid(row=7 , column=2 )
button_subtract.grid(row=2 , column=1 )
buttonEQUAL.grid(row=6 , column=3 )
buttonA.grid(row=3 , column=0 )
buttonB.grid(row=3 , column=1 )
buttonC.grid(row=3 , column=2 )
buttonD.grid(row=3 , column=3 )
buttonE.grid(row=4 , column=3 )
buttonF.grid(row=5 , column=3 )

button0o.grid(row=1 , column=0 )
button0x.grid(row=1 , column=2 )
button0b.grid(row=1 , column=1 )
button0d.grid(row=1 , column=3 )

buttono.grid(row=8 , column=0 )
buttonx.grid(row=8 , column=1 )
buttonb.grid(row=8 , column=2 )


'''placing the buttons end'''








root.mainloop()