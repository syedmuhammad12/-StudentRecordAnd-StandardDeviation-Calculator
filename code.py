# Importing Modules

from tkinter import *
from tkinter.messagebox import showinfo

# Reteriving file data into list
def listmake():
     with open("record.txt","r+") as f:
          d = []
          c= f.readlines()
          for i in c:
               if "\n" in i:
                    d.append(i[:-1])
               else:
                    d.append(i)
          e = []
          for i in range(3):
               e.append(d[i::3])
          g = []
          for i in e:
               for j in i:
                    g.append(j)
          h = []
          for i in g:
               t = i.split("\t")
               h.append(t)
     return h

# Creating a file
def filemake():
     with open("record.txt","w") as f:
          f.write("Student Name"+"\t"+"Roll No"+"\t"+"Marks")

# Function to add data in the file
def entry():
     try:
          with open("record.txt","r+") as f:
               pass
          with open("record.txt","a+") as f:
               f.write("\n"+f"{name.get()}"+"\t"+f"{roll.get()}"+"\t"+f"{marks.get()}")
     except:
          showinfo(message="Please create a file first")

# Function to create average class marks
def avg():
     try:
          with open("record.txt","r+") as f:
               d = []
               c= f.readlines()
               for i in c:
                    if "\n" in i:
                         d.append(i[:-1])
                    else:
                         d.append(i)
               e = []
               for i in range(3):
                    e.append(d[i::3])
               g = []
               for i in e:
                    for j in i:
                         g.append(j)
               h = []
               for i in g:
                    t = i.split("\t")
                    h.append(t)
          count = 0
          sum = 0
          for i in range(len(h)):
             if i>=1:
                 sum+=float(h[i][2])
                 count+=1
          avg = sum/count
          showinfo(message=f"The average marks of the class is {avg}")
     except:
          showinfo(message="No file found")

# Function to calculate Standard deviation of the class
def sd():
     try:
          with open("record.txt","r+") as f:
               d = []
               c= f.readlines()
               for i in c:
                    if "\n" in i:
                         d.append(i[:-1])
                    else:
                         d.append(i)
               e = []
               for i in range(3):
                    e.append(d[i::3])
               g = []
               for i in e:
                    for j in i:
                         g.append(j)
               h = []
               for i in g:
                    t = i.split("\t")
                    h.append(t)
          count = 0
          sum = 0
          for i in range(len(h)):
             if i>=1:
                 sum+=float(h[i][2])
                 count+=1
          avg = sum/count
          counter = 0
          for i in range(len(h)):
             if i>=1:
                 counter+=(float(h[i][2])-avg)**2
          sd = round((counter/(len(h)-2))**0.5,2)
          showinfo(message=f"Student deviation is {sd}")    
     except:
          showinfo(message="No file found")

# Main Program

a = Tk()
a.title("Database")
a.geometry("800x550+300+60")
a.maxsize("800","550")
a.minsize("800","550")
a.configure(bg="#9BCFD0")
name = StringVar()
roll = StringVar()
marks = StringVar()
l = Label(a,text= "Students Record",font=("Times New Roman","35","bold"),background="#9BCFD0")
l.pack()
f = Frame(a,background="#9BCFD0")
l = Label(f,text="Want to make a new file?",font="lucids 11 bold",background="#9BCFD0")
l.pack(side=LEFT,anchor="w",padx=30,pady=10)
b = Button(a,text="Create File First",font="lucida 11 bold",borderwidth=5,relief="groove",command=filemake) 
b.pack(side=RIGHT,anchor="n",pady=20,padx=50)
f.pack(pady= 20,anchor="w",padx=20)
f = Frame(a,background="#9BCFD0")
l = Label(f,text="Enter name of the student:",font="lucids 11 bold",background="#9BCFD0")
l.pack(side=LEFT,anchor="w",padx=30)
e = Entry(f,font="lucida 11 bold",textvar=name)
e.pack(ipadx=20,fill=X,padx=20)
f.pack(pady= 20,anchor="w",padx=20)
f = Frame(a,background="#9BCFD0")
l = Label(f,text="Enter Roll no of the student:",font="lucids 11 bold",background="#9BCFD0")
l.pack(side=LEFT,anchor="w",padx=30)
e = Entry(f,font="lucida 11 bold",textvar=roll)
e.pack(ipadx=20,fill=X,padx=6)
f.pack(pady= 20,anchor="w",padx=20)
f = Frame(a,background="#9BCFD0")
l = Label(f,text="Enter marks of the student:",font="lucids 11 bold",background="#9BCFD0")
l.pack(side=LEFT,anchor="w",padx=30)
e = Entry(f,font="lucida 11 bold",textvar=marks)
e.pack(ipadx=20,fill=X,padx=12)
f.pack(pady= 20,anchor="w",padx=20)
b = Button(a,text="Submit Entry",font="lucida 11 bold",borderwidth=5,relief="groove",command=entry) 
b.pack(pady=10)
l = Label(a,text="Other options",font=("Times New Roman","25","bold"),background="#9BCFD0")
l.pack(anchor="w",padx=40,pady=10)
f = Frame(a)
b = Button(a,text="Average",font="lucida 11 bold",borderwidth=5,relief="groove",command=avg) 
b.pack(anchor='nw',side=LEFT,padx=30,pady=10)
b = Button(a,text="Standard Deviation",font="lucida 11 bold",borderwidth=5,relief="groove",command=sd) 
b.pack(anchor='n',pady=10)
f.pack(pady= 20,padx=20)
a.mainloop()
