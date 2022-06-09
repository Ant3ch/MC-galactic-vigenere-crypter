from tkinter import *
import os
from files import chiffrement

font = "minecraft-enchantment.ttf"


def crypte_vigenre_galactic():
    inp = box.get(1.0, "end-1c")
    inp2 = box_key.get(1.0, "end-1c")
    if inp2 == "" or inp2 == " " or inp == "" or inp == " ":
        popup = Toplevel(root)
        popup.geometry("294x150")
        popup.title("WARNING")
        popup.iconbitmap('files/error.ico')
        Label(popup, text="You forget to put a \"key\" or a \"Message\"", font=('ARIAL')).place(relx=.5, rely=.5, anchor=S)
        popup.after(2000,lambda:popup.destroy() )
    inp = chiffrement.chiffrage_vigenere(inp, inp2)
    print(inp)
    inp = chiffrement.chiffrage_minecraftien(inp)
    print(inp)
    if inp:
        with open("result.txt", "wb") as file:
            file.write(bytes(inp.encode("utf8")))
    box.delete(1.0, "end")
    box.insert(1.0, inp)


def decrypte_vigenre_galactic():
    inp = box.get(1.0, "end-1c")
    inp2 = box_key.get(1.0, "end-1c")
    if inp2 == "" or inp2 == " " or inp == "" or inp == " ":
        popup = Toplevel(root)
        popup.geometry("294x150")
        popup.title("WARNING")
        popup.iconbitmap('files/error.ico')
        Label(popup, text="You forget to put a \"key\" or a \"Message\"", font=('ARIAL')).place(relx=.5, rely=.5,
                                                                                                anchor=S)
        popup.after(2000, lambda: popup.destroy())
    inp = chiffrement.dechiffrage_minecraftien(inp)
    inp = chiffrement.dechiffrage_vigenere(inp, inp2)
    with open("result.txt", "wb") as file:
        file.write(bytes(inp.encode("utf8")))
    box.delete(1.0, "end")
    box.insert(1.0, inp)


def generate_rdm_key():
    key = chiffrement.create_random_password(chiffrement.random.randint(3, 6))
    box_key.delete(1.0, "end")
    box_key.insert(1.0, key)


root = Tk()
root.wm_attributes("-transparentcolor", 'grey')

root.title("MC Galactic Vigenere ")
root.geometry("500x500")
root.resizable(False, False)
bg = PhotoImage(file="files/Bg.png")
root.iconbitmap("files/flavicon.ico")

back = Label(root, image=bg)
back.place(x=-10, y=-10)

lab = Label(root, text="crypter/decrypter", font=("Arial", 30))
lab.place(relx=.5, rely=.40, anchor=CENTER)

box = Text(root, height=1, width=30)
box.place(relx=.5, rely=.5, anchor=CENTER)

box_key = Text(root, height=1, width=10)
box_key.place(relx=.85, rely=.5, anchor=CENTER)

txt_key = Label(root, text="key", font=("Arial", 10))
txt_key.place(relx=.85, rely=.45, anchor=CENTER)

sumbit = Button(root, command=crypte_vigenre_galactic, text="crypte ! ")
sumbit.place(relx=.5, rely=.58, anchor=CENTER)

sumbit_2 = Button(root, command=decrypte_vigenre_galactic, text="decrypte ! ")
sumbit_2.place(relx=.5, rely=.70, anchor=CENTER)

rdm_key = Button(root, command=generate_rdm_key, text="Random key")
rdm_key.place(relx=.85, rely=.58, anchor=CENTER)

mf = Frame(root, width=80, height=80, bg="grey")
mf.place(relx=.2, rely=.7, anchor=CENTER)

Label(root, text="A hole in my code !").place(relx=.2, rely=.8, anchor=CENTER)
root.mainloop()
