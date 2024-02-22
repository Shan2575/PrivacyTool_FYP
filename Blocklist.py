from tkinter.messagebox import askyesno
import tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

####################
# Blocklist Methods


def addDomain():
    blocklistLB.insert(END, enterText.get())
    with open("domains.txt", 'w') as file:
        file.write('\n'.join(blocklistLB.get(0, END)))
        file.close()
    enterText.delete(0, END)


def deleteDomain():
    blocklistLB.delete(blocklistLB.curselection())
    with open("domains.txt", 'w') as file:
        file.write(''.join(blocklistLB.get(0, END)))
        file.close()


def deleteAllDomains():
    answer = askyesno(title='Delete all Domains',
                      message='Are you sure that you want to delete all Domains from the Blocklist?')
    if answer:
        blocklistLB.delete(0, END)
        with open("domains.txt", 'w') as file:
            file.write(''.join(blocklistLB.get(0, END)))
            file.close()


def goToCurrentCookiesWindow():
    window.destroy()
    import CurrentCookies


def goToAllCookiesWindow():
    window.destroy()
    import AllCookies


###############
# TKinter GUI

window = tkinter.Tk()
window.title('Browser Privacy Tool')
window.geometry('1000x550')
window.resizable(False, False)
window.configure(bg='snow3')

###############################
# TKinter Treeview Table Frame

table_frame = LabelFrame(window, text="Blocklist")
table_frame.grid(row=0, column=0, sticky=NW, padx=(10, 0), pady=(2, 0))
table_frame.configure(bg='snow3')

blocklistLB = Listbox(table_frame, height=25, width=130)
blocklistLB.grid(padx=5, pady=0)
file = open("domains.txt", "r")
for i in file:
    blocklistLB.insert(END, i)

label = Label(table_frame, text="Add a new Domain here:  ", bg='snow3')
label.grid(sticky=W, row=2, column=0, padx=(7, 0))

enterText = Entry(table_frame, width=30)
enterText.grid(sticky=W, row=2, column=0, padx=(145, 0), pady=5)

vertSB = Scrollbar(table_frame, command=blocklistLB.yview)
vertSB.place(x=771, y=2, height=402)
blocklistLB.config(yscrollcommand=vertSB.set)

#######################################
# TKinter Treeview Table Buttons Frame

table_frame_buttons = Frame(window)
table_frame_buttons.configure(bg='snow3')
table_frame_buttons.grid(row=2, column=0, sticky=W, padx=90, pady=20)

addDomImage = Image.open('images/addDomain.png')
resized_addDomImage = addDomImage.resize((30, 30), Image.LANCZOS)
refreshImage = ImageTk.PhotoImage(resized_addDomImage)
addDomainButton = Button(
    table_frame_buttons, text="Add Domain", command=addDomain, height=35, image=refreshImage, compound="left", padx=10)
addDomainButton.grid(row=2, column=0, padx=20)

delImage = Image.open('images/delete1.png')
resized_delImage = delImage.resize((30, 30), Image.LANCZOS)
deleteImage = ImageTk.PhotoImage(resized_delImage)
deleteButton = Button(
    table_frame_buttons, text="Delete Selected Domain", command=deleteDomain, height=35, image=deleteImage, compound="left", padx=10)
deleteButton.grid(row=2, column=1, padx=20)

delAllImage = Image.open('images/deleteAll.png')
resized_delAllImage = delAllImage.resize((30, 30), Image.LANCZOS)
deleteAllImage = ImageTk.PhotoImage(resized_delAllImage)
deleteAllButton = Button(
    table_frame_buttons, text="Delete All Domains", command=deleteAllDomains, height=35, image=deleteAllImage, compound="left", padx=10)
deleteAllButton.grid(row=2, column=2, padx=20)

#######################
# Sidebar Menu Buttons

menu_Frame = LabelFrame(window, text="Menu")
menu_Frame.configure(bg='snow3')
menu_Frame.grid(row=0, column=3, padx=(2, 5), pady=(2, 0), sticky=NE)

allCookiesButton = Button(
    menu_Frame, text="View All Cookies", command=goToAllCookiesWindow, width=15, padx=20, pady=20).pack(padx=15, pady=(80, 15))
currentCookiesButton = Button(
    menu_Frame, text="View Current Cookies", command=goToCurrentCookiesWindow, width=15, padx=20, pady=20).pack(padx=15, pady=15)
blocklistsButton = Button(
    menu_Frame, text="View Domain Blocklist", width=15, padx=20, pady=20).pack(padx=15, pady=(15, 99))

###################
# Window Mainloop

# window.after(10, refresh_program)
window.mainloop()
