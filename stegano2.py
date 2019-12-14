from tkinter import *
from tkinter import filedialog
from stegano import lsb,exifHeader
from PIL import Image
from tkinter import messagebox

file=""
def browseimg(img):
    try:
        global file
        file=filedialog.askopenfilename(filetypes=(("png files","*.png"),("jpg files","*.jpg"),("jpeg files","*.jpeg")))
        img.set(file)
    except:
        print("Something wrong")

def encode(img,msg):
    try:
        global file
        print(msg)
        file1=img
        crypfile=exifHeader.hide(file1,'secre.jpg',secret_message=msg)
        messagebox.showinfo("Done","Sucessfully done")
    except:
        print("Something wrong")

def decrypt(showmsg):
    try:
        efile=filedialog.askopenfilename(filetypes=(("png files","*.png"),("jpg files","*.jpg"),("jpeg files","*.jpeg")))
        emsg=exifHeader.reveal(efile)
        showmsg.set(emsg)
    except:
        print("Something wrong")

def originalshow():
    Image.open(file).show()
def show():
    encrypimg=Image.open("secre.jpg").show()

def encrypting():
    root1=Toplevel(root)
    root1.title("Encryption")
    root1.resizable(0,0)
    root1.geometry("450x350")
    root1.configure(bg="grey")
    img=StringVar()
    msg=StringVar()
    e1=Entry(root1,width=30,textvariable=img).grid(row=0,column=1,rowspan=4,columnspan=2,padx=10,pady=10)
    b1=Button(root1,text="Browse",width=20,command=lambda:browseimg(img)).grid(row=5,column=2,padx=10,pady=10)
    b3=Button(root1,text="Show original",width=20,command=lambda:originalshow()).grid(row=5,column=3,padx=10,pady=10)
    e2=Entry(root1,width=30,textvariable=msg).grid(row=6,column=1,rowspan=3,columnspan=2,padx=10,pady=10)
    b2=Button(root1,width=20,text="Send",command=lambda:encode(img.get(),msg.get())).grid(row=10,column=2,padx=10,pady=10)
    b3=Button(root1,width=20,text="Show",command=lambda:show()).grid(row=10,column=3,padx=10,pady=10)
    root1.mainloop()

def decrypting():
    root2=Toplevel(root)
    root2.title("Decryption")
    root2.resizable(0,0)
    root2.geometry("600x300")
    root2.configure(bg="black")
    showmsg = StringVar()
    b1=Button(root2,text="Show Picture",width=30,command=lambda:show()).grid(row=0,column=0,padx=10,pady=10)
    b2=Button(root2,text="Show Message",width=30,command=lambda:decrypt(showmsg)).grid(row=1,column=0,padx=10,pady=10)
    e1=Entry(root2,textvariable=showmsg,width=50).grid(row=1,column=1,padx=10,pady=10)


root=Tk()
root.title("Spychat")
root.resizable(0,0)
root.geometry("300x150")
root.configure(bg="teal")
b1=Button(root,text="Encrypt",width=30,command=lambda:encrypting()).grid(row=0,column=0,padx=10,pady=10)
b2=Button(root,text="Decrypt",width=30,command=lambda:decrypting()).grid(row=1,column=0,padx=10,pady=10)
root.mainloop()