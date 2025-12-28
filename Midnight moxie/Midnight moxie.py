import requests
import io
import random
from tkinter import * 
from tkinter import filedialog #responsible for reading files
from PIL import ImageTk, Image

root=Tk() #assigning class to object
root.resizable(0,0)
root.title("Midnight Moxie Bar-back")
root.geometry("555x600")
root['bg']="#1b1b1b"

img1 = Image.open("Shirley idle.png") 
img1 = img1.resize((300,388))
sherIdle= ImageTk.PhotoImage(img1)

img2 = Image.open("Shirley talk.png")
img2 = img2.resize((300,388))
sherTalk= ImageTk.PhotoImage(img2)

img3 = Image.open("Shirley Whut.png") 
img3 = img3.resize((300,388))
sherWhut= ImageTk.PhotoImage(img3)

#^^^ These PNGs are made by me

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=2)
root.columnconfigure(3, weight=2)

def whut(): #Error frame
    huh = ["I'm sorry?", "Could you repeat that, please?", "What was that?", "Hmm?", "Come again?"]
    err = random.choice(huh) #Randomly pull from these ^^^
    txta1.delete("1.0","end")
    txta2.delete("1.0","end")
    Shirley.config(image=sherWhut)
    drinkName.config(text=err)

def recipe(drinks):
    txta1.delete("1.0","end")
    txta2.delete("1.0","end")
    x = 0
    ingredients = []
    while True:
        x += 1
        if (drinks[0][f'strMeasure{x}']) == None and (drinks[0][f'strIngredient{x}']) == None:
            break #If there are no measurements or ingredients, Break
        else:
            if (drinks[0][f'strMeasure{x}']) != None: measure = drinks[0][f'strMeasure{x}']
            else: measure = "" #If there are no measuremente, Return blank ()
            if (drinks[0][f'strIngredient{x}']) != None: ingredient = drinks[0][f'strIngredient{x}'].capitalize()
            else: break #If there are no ingredients, Break
            ingredients.append(f"{measure} {ingredient}\n")
    instructions = drinks[0]['strInstructions']
    if not ingredients:txta1.insert(END,"Oops! No ingredients provided for this one!")
    else: 
        for i in ingredients: txta1.insert(END,i) #Loop through and put every ngredient into text box
    if instructions == None: txta2.insert(END,"Oops! No intructions provided for this one!")
    else:txta2.insert(END,instructions)

def orderup(url):
    response = requests.get(url)
    data = response.json()
    drinks = data["drinks"]
    Shirley.config(image=sherTalk)
    #Trying to show drink name (incase of failed search)
    try:
        Drink_name = drinks[0]['strDrink'] # Access Drink name
        drinkName.config(text=Drink_name)
    except: whut()
    else: #Display drink image
        image_url = drinks[0]['strDrinkThumb'] # Access Drink image url
        image_response = requests.get(image_url)
        if image_response.status_code == 200:
            image = Image.open(io.BytesIO(image_response.content)) 
            image = image.resize((80,80))
            image = ImageTk.PhotoImage(image) 
            image_label = Label(root, image=image, bg="#1b1b1b") # keep a reference to the image to prevent garbage collection 
            image_label.image = image
            image_label.grid(row=2,column=0,rowspan=3,columnspan=1)
        else: #If an image is not available, use mystery drink (Png made by me)
            img4 = Image.open("mystery juice.png") 
            img4 = img4.resize((80,80))
            phdrink= ImageTk.PhotoImage(img4)
            image_label = Label(root, image=phdrink, bg="#1b1b1b")
            image_label.image = phdrink
            image_label.grid(row=2,column=0,rowspan=3,columnspan=1)
        recipe(drinks) #output ingredients and recipe

def surpriseme():
    url = "https://www.thecocktaildb.com/api/json/v1/1/random.php" #SPIN THE WHEEL!
    orderup(url)

def orderdrink():
    search = txt.get() #Take input from textbox
    url= f"https://www.thecocktaildb.com/api/json/v1/1/search.php?s={search}"
    orderup(url)
    

MM = Label(root, text="Midnight Moxie" ,font=('Georgia Bold',22), bg='#1b1b1b',fg="#F4B71D")
MM.grid(row=0,column=0,columnspan=4,sticky="ew", pady=5)

Shirley = Label(root, image=sherIdle, bg="#1b1b1b", highlightthickness=2, highlightbackground= "white")
Shirley.grid(row=1,column=0, columnspan=2, rowspan=2)

drinkName = Label(root, text="Serving..." ,font=('Georgia',17), bg='#1b1b1b',fg="white", wraplength=200)
drinkName.grid(row=1, column=3, sticky="n",columnspan=4)

txta1=Text(root, width=25, height=15, bg="#2f2f2f", fg="white", relief="flat", wrap='word', highlightthickness=5, highlightbackground = "#783F1A", font=('Verdana',10))
txta1.grid(row=1, column=3,rowspan=3, columnspan=5)

txt = Entry(root, relief="flat",bg="white")
txt.grid(row=5,column=0, columnspan=2, sticky="ew", padx=20)

b1 = Button(root, text="Order", command=orderdrink, width=20,height=1,bg="#F4B71D",fg="#1F1400", relief="flat",font=('Lucida Console',10))
b1.grid(row=5,column=2,columnspan=3, pady=5)

b2 = Button(root, text="Surprise me", command=surpriseme, width=20,height=1,bg="#F4B71D",fg="#1F1400", relief="flat",font=('Lucida Console',10))
b2.grid(row=6,column=0,columnspan=2,pady=5)

txta2=Text(root, width=20, height=4, bg="#2f2f2f", fg="white", relief="flat", bd=2, wrap='word',highlightthickness=5, highlightbackground = "#783F1A", font=('Verdana',10))
txta2.grid(row=7, column=0,columnspan=5,sticky="nsew",padx=20, pady=5)

scrollV = Scrollbar(root,orient='vertical', command=txta2.yview)
scrollV.grid(row=7,column=4,sticky='ns')
txta2.config(yscrollcommand=scrollV.set)


root.mainloop()
