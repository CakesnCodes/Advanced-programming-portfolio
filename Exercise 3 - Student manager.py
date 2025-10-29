# -*- coding: utf-8 -*-
"""
Created on Mon Oct 20 13:41:31 2025

@author: User
"""

from tkinter import * 
from tkinter import filedialog, ttk
root = Tk()

root.geometry("500x350")
root.resizable(0,0)

with open("studentMarks.txt") as file_handler: #opens and reads files
    records = file_handler.read()
    out = [line.split(",") for line in records.split('\n')] #courtesy of user7864386
    #splits lines into a list of strings which are then split further into a list of strings

names = [row[1] for row in out[1:]] #takes the names from the records and puts them into a list

class student: #first class in an assessment
    def __init__(self, name, classnumber, c1,c2,c3,exammark): #assigns values into object properties
        self.num = classnumber
        self.fname = name
        self.cwTotal = int(c1)+int(c2)+int(c3) #sum of all course scores
        self.examMark = exammark 
        self.overall = (int(self.cwTotal)/ 160) * 100 #divides coursework total from total score and times to 100 to get overal percentage
        self.grade = markGrade(int(self.examMark)) #assigns a rank via a function
    def info(self): #prints student information based on info above ^^
        return f"""Name: {self.num}
Number: {self.fname}
Coursework Total: {self.cwTotal}
Exam Mark {self.examMark}
Overall Percentage: %{self.overall}
Grade: {self.grade}

"""

def markGrade(mark): #returns grades based on overall marks
    if mark >= 70:return "A"
    if mark <= 69 and mark >= 60 :return "B"
    if mark <= 59 and mark >= 50 :return "C"
    if mark <= 49 and mark >= 40 :return "D"
    if mark < 40 :return "F"

def viewall(): #Prints all records
    txtarea.delete("1.0","end") #sets text area to blank
    content=[]
    for i in range(1, len(out)): #for item in range of amount of items in out
        record = student(out[i][0],out[i][1],out[i][2],out[i][3],out[i][4],out[i][5])
        content.append(record.info()) #add info to content list
    for j in content:
        txtarea.insert(END,j) #print students info
        print(j)    

def viewStudent(): #displays student selected from combo box
    txtarea.delete("1.0","end")
    search = cb.get()  #gets value from combo box
    for i in range (1, len(out)):
        if out[i][1]==search: # if the student name is found in list
            record = student(out[i][0],out[i][1],out[i][2],out[i][3],out[i][4],out[i][5]) #put index num of student though the class
            content=(record.info())
    txtarea.insert(END,content) #print student info
    print(content) 

def highest():#finds the student with the highest score
    txtarea.delete("1.0","end") #clears text area
    scores = [((int(row[2]) + int(row[3]) + int(row[4]))/ 160) * 100 for row in out[1:]] #creates list of all student's overall percentages
    i = scores.index(max(scores))+1 #assign index of the largest percentage (+1) to i
    record = student(out[i][0],out[i][1],out[i][2],out[i][3],out[i][4],out[i][5])
    content=(record.info())
    txtarea.insert(END,content)
    print(content)

def lowest():#finds the student with the lowest score
    #works similarly to 'highest()' function
    txtarea.delete("1.0","end") #clears text area
    scores = [((int(row[2]) + int(row[3]) + int(row[4]))/ 160) * 100 for row in out[1:]]
    i = scores.index(min(scores))+1 #assign index of the lowest percentage (+1) to i
    record = student(out[i][0],out[i][1],out[i][2],out[i][3],out[i][4],out[i][5])
    content=(record.info())
    txtarea.insert(END,content)
    print(content)
	

label = Label(root, text="Student Records Manager", font=("Courier New",10)).grid(row=0,column=1,sticky="ew",pady=10)

#buttons
b1 = Button(root,text="View all Records",command=viewall,font=("Courier New",10)).grid(row=1,column=0,padx=5)
b2 = Button(root,text="Show Highest Score",command=highest,font=("Courier New",10)).grid(row=1,column=1, padx=5)
b3 = Button(root,text="Show Lowest Score",command=lowest,font=("Courier New",10)).grid(row=1,column=2, padx=5)

#combo box
label = Label(root, text="Student:", font=("Courier New",10)).grid(row=2,column=0,pady=5)
cb = ttk.Combobox(root, values=names)
cb.set("Jake Hobbs")
cb.grid(row=2,column=1,pady=5)
b4 = Button(root,text="View Record",command=viewStudent,font=("Courier New",10)).grid(row=2,column=2,pady=5) #button to submit cb selection

#text area
txtarea=Text(root, width=44, height=12)
txtarea.grid(row=3,column=0, columnspan=3)

#scroll bar
scrollV = Scrollbar(root,orient='vertical', command=txtarea.yview)
scrollV.grid(row=3,column=2,sticky='ns')
txtarea.config(yscrollcommand=scrollV.set)

root.mainloop()