import os
import sqlite3
import tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

#############################################################################################
# CurrentCookies Methods


def goToAllCookiesWindow():
    window.destroy()
    import AllCookies


def goToBlocklistWindow():
    window.destroy()
    import Blocklist

#############################################################################################
# TKinter GUI


window = tkinter.Tk()
window.title('Browser Privacy Tool')
window.geometry('1000x550')
window.resizable(False, False)
window.configure(bg='snow3')


#############################################################################################
# TKinter Treeview Table Frame


table_frame = LabelFrame(window, text="Current Cookies")
table_frame.grid(row=0, column=0, sticky=NW, padx=(10, 0), pady=(2, 0))
table_frame.configure(bg='snow3')

cookie_table = ttk.Treeview(table_frame, height=20)
cookie_table.grid(row=0, column=0, padx=5, pady=(0, 5))
cookie_table['columns'] = ('row_no', 'domain_name',
                           'cookieID', 'isHTTPOnly', 'creation', 'expiry')

vertSB = ttk.Scrollbar(table_frame, command=cookie_table.yview)
vertSB.configure(command=cookie_table.yview)

cookie_table.tag_configure('oddRow', background="white")
cookie_table.tag_configure('evenRow', background="light grey")
cookie_table.column('#0', width=0, stretch=NO)
cookie_table.column('row_no', anchor=W, width=27)
cookie_table.column('domain_name', anchor=W, width=200)
cookie_table.column('cookieID', anchor=W, width=180)
cookie_table.column('isHTTPOnly', anchor=CENTER, width=69)
cookie_table.column('creation', anchor=W, width=150)
cookie_table.column('expiry', anchor=W, width=150)

cookie_table.heading('#0')
cookie_table.heading('row_no', text='No.', anchor=W)
cookie_table.heading('domain_name', text='Domain Name', anchor=W)
cookie_table.heading('cookieID', text='CookieID', anchor=W)
cookie_table.heading('isHTTPOnly', text='isHTTPOnly', anchor=W)
cookie_table.heading('creation', text='Creation_UTC', anchor=W)
cookie_table.heading('expiry', text='Expiry_UTC', anchor=W)


#############################################################################################
# TKinter Treeview Table Buttons Frame

table_frame_buttons = Frame(window)
table_frame_buttons.configure(bg='snow3')
table_frame_buttons.grid(row=1, column=0, sticky=W, padx=90, pady=20)

rImage = Image.open('images/Refresh_icon.png')
resized_rImage = rImage.resize((30, 30), Image.LANCZOS)
refreshImage = ImageTk.PhotoImage(resized_rImage)
refreshButton = Button(
    table_frame_buttons, text="Refresh Cookies", height=35, image=refreshImage, compound="left", padx=10)
refreshButton.grid(row=1, column=0, padx=20)

delImage = Image.open('images/delete1.png')
resized_delImage = delImage.resize((30, 30), Image.LANCZOS)
deleteImage = ImageTk.PhotoImage(resized_delImage)
deleteButton = Button(
    table_frame_buttons, text="Delete Selected Cookies", height=35, image=deleteImage, compound="left", padx=10)
deleteButton.grid(row=1, column=1, padx=20)

delAllImage = Image.open('images/deleteAll.png')
resized_delAllImage = delAllImage.resize((30, 30), Image.LANCZOS)
deleteAllImage = ImageTk.PhotoImage(resized_delAllImage)
deleteAllButton = Button(
    table_frame_buttons, text="Delete All Cookies", height=35, image=deleteAllImage, compound="left", padx=10)
deleteAllButton.grid(row=1, column=2, padx=20)

#############################################################################################
# Sidebar Menu Buttons

menu_Frame = LabelFrame(window, text="Menu")
menu_Frame.configure(bg='snow3')
menu_Frame.grid(row=0, column=3, padx=(2, 5), pady=(2, 0), sticky=NE)

allCookiesButton = Button(
    menu_Frame, text="View All Cookies", command=goToAllCookiesWindow, width=15, padx=20, pady=20).pack(padx=15, pady=(80, 15))
currentCookiesButton = Button(
    menu_Frame, text="View Current Cookies", width=15, padx=20, pady=20).pack(padx=15, pady=15)
blocklistsButton = Button(
    menu_Frame, text="View Domain Blocklist", command=goToBlocklistWindow, width=15, padx=20, pady=20).pack(padx=15, pady=(15, 99))

#############################################################################################
# Window Mainloop

#window.after(10, refresh_program)
window.mainloop()
