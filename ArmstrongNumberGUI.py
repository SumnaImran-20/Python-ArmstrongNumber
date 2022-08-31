#importing libraries
from ast import Pass
from tkinter import *
from turtle import bgcolor
from tkinter import messagebox

#LOGIC FOR ARMSTRONG NUMBER
def check():
    if(b['text']=='Check'):
        b['text']='Checked'
    else:
        b['text']='Check'
    
    print("---Program to check 3 digit Armstrong Number---")
    if numbervalue.get() >= 100 and numbervalue.get() <= 999:
     print("You entered the number within the range: ",numbervalue.get())
     messagebox.showinfo('Result', 'You entered the number within the range')
     sum = 0
    
     #find the sum of cube of of each digit
     temp = numbervalue.get()
     while temp>0:
      digit = temp % 10
      sum += digit**3
      temp//= 10

     #display the result
     if sum ==numbervalue.get():
      print("This is an armstrong number: ",numbervalue.get())
      messagebox.showinfo('Result', 'This is an armstrong number')
     else:
      print("This is not an armstrong number: ",numbervalue.get())
      messagebox.showinfo('Result', 'This is not an armstrong number')
    
    else:
        print("You did not entered the number with in range: ",numbervalue.get())
        messagebox.showinfo('Result', 'You did not entered the number with in range. Please try again')
    print("---The End---")
    

#GUI FOR DISPLAYIG THE RESULT
demo_root = Tk()
demo_root.title("Armstrong Program")

#Geometry of the box
demo_root.geometry("700x434")
#Set Window Color
demo_root['background'] = '#856ff8'

#Size of the box
demo_root.minsize(300,100)
demo_root.maxsize(1200,988)

#label of the boxtext="Enter Number to Check: "
txt = Label(demo_root,text="Program to check armstrong number between 100-999",font=("Raleway",15,"bold"),padx=20,pady=20,
bg='#856ff8')
txt.grid(row=0)
number = Label(demo_root,text="Enter Number: ")
number.grid(row=1)
numbervalue = IntVar()
numberentry = Entry(demo_root,textvariable=numbervalue)
numberentry.grid(row = 1, column=1)

#Button
b=Button(fg="black",text="Check",command=check)
b.grid(column=1, row=3,padx=5, pady=10)

demo_root.mainloop()
