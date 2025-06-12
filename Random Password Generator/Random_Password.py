import tkinter as tk
from tkinter import ttk
import pyperclip as clip
import random
import string

randy=""
remove=[]

def password():
    global randy,remove
    randy=""
    pword=[]
    leng=int(maxlen.get())
    remove=to_remove.get().split()
    try:
        if leng>2 and leng<15:
            i=0
            while(i<leng):
                l=random.randint(0,3)                    
                if check_special.get()==1 and l==1:
                    pword.append(random.choice(string.punctuation))
                    i+=1
                    continue
                if check_upper.get()==1 and l==2:
                    pword.append(random.choice(string.ascii_uppercase))
                    i+=1
                    continue
                if check_number.get()==1 and l==3:
                    pword.append(random.choice(string.digits))
                    i+=1
                    continue
                else:
                    pword.append(random.choice(string.ascii_lowercase))
                    i+=1
                    continue
            randy=randy.join(pword)
            for i in range(len(remove)):
                randy=randy.replace(remove[i],"")
            if len(randy)==leng:
                newpass.set(randy)
            else:
                password
            message.set("")
        else:
            message.set("Invalid length")
            return None
        
    except ValueError:
        message.set("Enter integer value")
        return None
    
def to_clip():
    clip.copy(randy)
    if randy=="":
        return None
    else:
        message.set("Password copied")

#window
randpass= tk.Tk()

#titles
randpass.title("Password Generator")
randpass.geometry("300x450")
randpass.resizable(False,False)

#variables
message=tk.StringVar()
check_special=tk.IntVar()
check_upper=tk.IntVar()
check_number=tk.IntVar()
maxlen=tk.StringVar()
newpass=tk.StringVar()
to_remove=tk.StringVar()


#labels
length=ttk.Label(randpass,text="Length of Password (between 3 & 14)",font=("DM sans",10))
options=ttk.Label(randpass,text="Options",font=("DM sans",10,"bold"))
message_label=ttk.Label(randpass,textvariable=message,font=("DM sans",10,"bold"))
exclude=ttk.Label(randpass,text="Exclude character\n(separate with space)",font=("DM sans",10,"bold"))

#entry
enter=ttk.Entry(randpass,textvariable=maxlen,justify="center")
Text=ttk.Entry(randpass,text="",textvariable=newpass,justify="center")
Remov=ttk.Entry(randpass,text="",textvariable=to_remove,justify="center")

#check buttons
Special=ttk.Checkbutton(randpass,text="Include Special Characters",variable=check_special,onvalue=1,offvalue=0)
Upper=ttk.Checkbutton(randpass,text="Include Upper Case",variable=check_upper,onvalue=1,offvalue=0)
Number=ttk.Checkbutton(randpass,text="Include Numbers",variable=check_number,onvalue=1,offvalue=0)
generate=ttk.Button(randpass,text="Generate", command=password) 
copy=ttk.Button(randpass,text="Copy",command=to_clip,width=5)

#packs
length.pack(anchor="w",padx=15,pady=5)
enter.pack(anchor="w",padx=15,pady=5)
options.pack(anchor="w",padx=10,pady=5)
Special.pack(anchor="w",padx=15,pady=5)
Upper.pack(anchor="w",padx=15,pady=5)
Number.pack(anchor="w",padx=15,pady=5)
exclude.pack(anchor="w",padx=15,pady=5)
Remov.pack(anchor="w",padx=15,pady=5)
generate.pack(pady=5)
Text.pack(pady=5)
copy.pack(pady=5)
message_label.pack(pady=10)


#run
randpass.mainloop()
