from tkinter import *
from tkinter import messagebox
# ---------------------------- UI SETUP ------------------------------- #


window =Tk()
window.title("PASSWORD MANAGER")
window.config(padx=20,pady=20)

canvas=Canvas(width=200,height=200)
photo=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=photo)
canvas.grid(column=1,row=0)

# WEBSITE
website=Label(text="Website:")
website.grid(column=0,row=1)

websiteE=Entry(width=35)
websiteE.grid(column=1,row=1,columnspan=2)
websiteE.focus()


# EMAIL
Email=Label(text="Email/Username:")
Email.grid(column=0,row=2)
EmailE=Entry(width=35)
EmailE.grid(column=1,row=2,columnspan=2)
EmailE.insert(END,"muhammadwaleedakhtar240@gmail.com")

# Password
Password=Label(text="Password:")
Password.grid(column=0,row=3)
PasswordE=Entry(width=17)
PasswordE.grid(column=1,row=3)
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
run=False
import random
def create():
    global run
    run=True
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
     password_list.append(random.choice(letters))

    for char in range(nr_symbols):
     password_list += random.choice(symbols)

    for char in range(nr_numbers):
     password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
     password += char
    PasswordE.insert(END,password)
    return password
    


genrate=Button(text="Genrate Password",width=15,command=create)
genrate.grid(column=2,row=3)



# ---------------------------- SAVE PASSWORD ------------------------------- #
import pandas as pd
lis=[]
def addValue():
    
    global run
    Name=websiteE.get()
    Email=EmailE.get()
    if run:
        passw=create()
        
        run=False
    else:    
     passw=PasswordE.get()
    
    if len(Name)==0 or len(Email)==0 or len(passw)==0:
        
        chk= messagebox.askokcancel(title="Warning",message="You Left Some Thing Empty")
    else:   
        ok=messagebox.askokcancel(title="Cheking",message=f"Email:f{Email}\n Name: f{Name} \n Password: {passw} \n Is it Correct Info")
        if ok:
            dic={"Name":F"{Name}","Email":f"{Email}","Password":f"{passw}"}
            lis.append(dic)
            var=pd.DataFrame(lis)
            with open("NEW FILE.txt",mode="+a") as file:
              file.write(f"{var}")
        
    
        
    












# ---------------------------- SAVE PASSWORD ------------------------------- #

# ADD
add=Button(text="ADD",width=30,command=addValue)
add.grid(column=1,row=4,columnspan=2)





window.mainloop()
