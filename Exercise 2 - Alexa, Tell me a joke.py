import random
from tkinter import * 
from tkinter import filedialog
root = Tk()

root.geometry("350x200")
root.resizable(0,0)

        
def rng():
    global num
    num= random.randrange(0, 36)
    if num % 2 != 0:
        num -= 1
        jokes(num)
    else:
        jokes(num)

def jokes(num):
    with open("randomJokes.txt", errors="ignore") as setup:
        joke = setup.readlines()
        l1.config(text= f"{joke[num]}")
        l2.config(text="")

        global why
        why = Button(root,text="  ?  ",command=cont,font=("Comic Sans MS",10))
        why.pack(pady=5, padx=5)
        ask.config()
        
def cont():
    with open("randomJokes.txt", errors="ignore") as setup:
        punch = setup.readlines()
        l2.config(text= f"{punch[num+1]}") 
        why.pack_forget()


l1 = Label(root,text=" ")
l1.pack(pady=15)

l2 = Label(root,text=" ")
l2.pack(pady=5,padx=5)
    

ask = Button(root,text="Alexa, tell me a joke",command=rng,font=("Comic Sans MS",10))
ask.pack(pady=10)



root.mainloop() #Opens application


