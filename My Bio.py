from tkinter import *
from PIL import  ImageTk, Image
import tkinter.messagebox as tmsg
root = Tk()
root.geometry("1000x1000")
root.title("Arindam Bio")

# Creating A Heading:
f = Frame(root)
f.pack()
Label(f,text='ARINDAM BIO',bg='Black',fg='yellow',font= "Nyala 30 bold").pack()

# Add A Image:
img = Image.open("1.png")
img = img.resize((225, 290), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(img)

#Adding Frame and attachted image:
f1 = Frame(root,borderwidth=5)
f1.pack(side=RIGHT,anchor='ne')
img1 = Label(f1, image=photo)
img1.pack()

f2 = Frame(root,borderwidth=10)
f2.pack(anchor='nw',pady=50)
Label(f2,text="Name:",font= "Arial 12 bold").grid(row=1,column=10)
Label(f2,text="Arindam Mondal",font= "CASTELLAR 10 bold").grid(row=1,column=11)
Label(f2,text="Address: ",font= "Arial 12 bold").grid(row=2,column=10)
Label(f2,text="GORAMAHAL,MOYNA,PURBA MEDINIPUR,721642",font= "CASTELLAR 10 bold").grid(row=2,column=11)
Label(f2,text="Phone:",font= "Arial 12 bold").grid(row=3,column=10)
Label(f2,text="+918327282965",font= "CASTELLAR 10 bold").grid(row=3,column=11)
Label(f2,text="Email:",font= "Arial 12 bold").grid(row=4,column=10)
Label(f2,text="marindam2017@gmail.com",font= "CASTELLAR 10 bold").grid(row=4,column=11)
Label(f2,text="Website: ",font= "Arial 12 bold").grid(row=5,column=10)
Label(f2,text="Codearindam.blogspot.com",font= "CASTELLAR 10 bold").grid(row=5,column=11)

f3 =Frame(root)
f3.pack(side=LEFT,anchor='nw',pady=1)
Label(f3,text="--More About Me--",font= "Roman 15 bold").pack()

f4 = Frame(f3,borderwidth=10)
f4.pack(anchor='nw')
Label(f4,text="Date Of Birth:",font= "Arial 12 bold").grid(row=1,column=1)
Label(f4,text="3rd October,1998",font= "Arial 10 bold").grid(row=1,column=4)
Label(f4,text="Religion:",font= "Arial 12 bold").grid(row=2,column=1)
Label(f4,text="Hindu",font= "Arial 10 bold").grid(row=2,column=4)
Label(f4,text="Father Name:",font= "Arial 12 bold").grid(row=3,column=1)
Label(f4,text="Arun Mondal",font= "Arial 10 bold").grid(row=3,column=4)
Label(f4,text="Hobbies:",font= "Arial 12 bold").grid(row=4,column=1)
Label(f4,text="Listen Music And Coding",font= "Arial 10 bold").grid(row=4,column=4)

f5 = Frame(root)
f5.pack(side=LEFT,anchor='nw',pady=150,padx=100)
Label(f5,text="---------EXTRA ABILITY---------",font= "Roman 15 underline").pack()

Label(f5,text="'Coding Is My Life And also like coding\nAlso in left in side website desginer\nlike to do Photo&Video Editing\nApp Devolopment\nPython Is Love'",font= "Arial 10 bold").pack()

photos = []
for i in range(0, 2):
    image = Image.open(f"{i+1}.png")
    #TODO: Resize these images
    image = image.resize((100, 100), Image.ANTIALIAS)
    photos.append(ImageTk.PhotoImage(image))

f6 = Frame(f3, width=900, height=200, pady=14, padx=22)
Label(f6, image=photos[1], anchor="w", padx=22).pack(anchor="sw",pady=20)
f6.pack(anchor="sw",pady=40)

# Adding Massafebar and menubars

def feedback():
    print("Hi guys This Is Arindam")
    tmsg.showinfo("CopyRight","Hi Dear All Guys This Is My CV")

mainmenu = Menu(root)
m1 = Menu(mainmenu,tearoff=0)
m1.add_command(label="Give Me A feedback",command=feedback)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Help",menu=m1)



root.mainloop()