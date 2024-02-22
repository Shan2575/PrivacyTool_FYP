import os
import sqlite3
import tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter.messagebox import askyesno
from datetime import datetime, timedelta

#####################
# AllCookies Methods

filename = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
                        "Google", "Chrome", "User Data", "Profile 1", "Network", "Cookies")

print("\n",filename,"\n")
connection = sqlite3.connect(filename)


def convertUTC(utc):
    try:
        return datetime(1601, 1, 1) + timedelta(microseconds=utc)
    except:
        pass


def getCookies():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM cookies")
    global results
    results = cursor.fetchall()


def refresh_program():
    getCookies()
    cookie_table.delete(*cookie_table.get_children())
    count = 0
    rowCount = 1

    for r in results:
        creationUTC = convertUTC(r[0])
        expiryUTC = convertUTC(r[7])
        if count % 2 == 0:
            cookie_table.insert(parent='', index='end', iid=count, text='', values=(
                rowCount, r[2], r[3], bool(r[9]), creationUTC, expiryUTC), tags=('evenRow',))
        else:
            cookie_table.insert(parent='', index='end', iid=count, text='', values=(
                rowCount, r[2], r[3], bool(r[9]), creationUTC, expiryUTC), tags=('oddRow',))
        count += 1
        rowCount += 1


def deleteDBRow(cookieName):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM cookies WHERE name=?", (cookieName,))
    connection.commit()


def deleteAllDB():
    answer = askyesno(title='Delete all Cookies',
                      message='Are you sure that you want to delete all Cookies from the System? This may result in saved logins and other important information being cleared from your browser.')
    if answer:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM cookies")
        connection.commit()
        refresh_program()


def deleteTableRow():
    os.system("taskkill /im chrome.exe /f")
    selectedRow = cookie_table.focus()
    rowvalues = cookie_table.item(selectedRow, 'values')
    cookieName = rowvalues[2]
    print('\n' + 'Cookie: "' + cookieName + '" was deleted from the system.')
    cookie_table.delete(selectedRow)
    deleteDBRow(cookieName)
    refresh_program()


def goToCurrentCookiesWindow():
    window.destroy()
    import CurrentCookies


def goToBlocklistWindow():
    window.destroy()
    import Blocklist

###############
# TKinter GUI


window = tkinter.Tk()
window.title('Browser Privacy Tool')
window.geometry('1000x550')
window.resizable(False, False)
window.configure(bg='snow3')


################################
# TKinter Treeview Table Frame


table_frame = LabelFrame(window, text="All Cookies")
table_frame.grid(row=0, column=0, sticky=NW, padx=(10, 0), pady=(2, 0))
table_frame.configure(bg='snow3')

cookie_table = ttk.Treeview(table_frame, height=20)
cookie_table.grid(row=0, column=0, padx=5, pady=(0, 5))
cookie_table['columns'] = ('row_no', 'domain_name',
                           'cookieID', 'isHTTPOnly', 'creation', 'expiry')

vertSB = Scrollbar(table_frame, command=cookie_table.yview)
vertSB.place(x=765, y=1, height=424)
cookie_table.config(yscrollcommand=vertSB.set)

cookie_table.tag_configure('oddRow', background="white")
cookie_table.tag_configure('evenRow', background="light grey")
cookie_table.column('#0', width=0, stretch=NO)
cookie_table.column('row_no', anchor=W, width=27)
cookie_table.column('domain_name', anchor=W, width=170)
cookie_table.column('cookieID', anchor=W, width=170)
cookie_table.column('isHTTPOnly', anchor=CENTER, width=69)
cookie_table.column('creation', anchor=W, width=160)
cookie_table.column('expiry', anchor=W, width=180)

cookie_table.heading('#0')
cookie_table.heading('row_no', text='No.', anchor=W)
cookie_table.heading('domain_name', text='Domain Name', anchor=W)
cookie_table.heading('cookieID', text='CookieID', anchor=W)
cookie_table.heading('isHTTPOnly', text='isHTTPOnly', anchor=W)
cookie_table.heading('creation', text='Creation_UTC', anchor=W)
cookie_table.heading('expiry', text='Expiry_UTC', anchor=W)


#######################################
# TKinter Treeview Table Buttons Frame

table_frame_buttons = Frame(window)
table_frame_buttons.configure(bg='snow3')
table_frame_buttons.grid(row=1, column=0, sticky=W, padx=90, pady=20)

rImage = Image.open('images/Refresh_icon.png')
resized_rImage = rImage.resize((30, 30), Image.LANCZOS )
refreshImage = ImageTk.PhotoImage(resized_rImage)
refreshButton = Button(
    table_frame_buttons, text="Refresh Cookies", command=refresh_program, height=35, image=refreshImage, compound="left", padx=10)
refreshButton.grid(row=1, column=0, padx=20)

delImage = Image.open('images/delete1.png')
resized_delImage = delImage.resize((30, 30), Image.LANCZOS )
deleteImage = ImageTk.PhotoImage(resized_delImage)
deleteButton = Button(
    table_frame_buttons, text="Delete Selected Cookies", command=deleteTableRow, height=35, image=deleteImage, compound="left", padx=10)
deleteButton.grid(row=1, column=1, padx=20)

delAllImage = Image.open('images/deleteAll.png')
resized_delAllImage = delAllImage.resize((30, 30), Image.LANCZOS )
deleteAllImage = ImageTk.PhotoImage(resized_delAllImage)
deleteAllButton = Button(
    table_frame_buttons, text="Delete All Cookies", command=deleteAllDB, height=35, image=deleteAllImage, compound="left", padx=10)
deleteAllButton.grid(row=1, column=2, padx=20)

#######################
# Sidebar Menu Buttons

menu_Frame = LabelFrame(window, text="Menu")
menu_Frame.configure(bg='snow3')
menu_Frame.grid(row=0, column=3, padx=(2, 5), pady=(2, 0), sticky=NE)

allCookiesButton = Button(
    menu_Frame, text="View All Cookies", width=15, padx=20, pady=20).pack(padx=15, pady=(80, 15))
currentCookiesButton = Button(
    menu_Frame, text="View Current Cookies", command=goToCurrentCookiesWindow, width=15, padx=20, pady=20).pack(padx=15, pady=15)
blocklistsButton = Button(
    menu_Frame, text="View Domain Blocklist", command=goToBlocklistWindow, width=15, padx=20, pady=20).pack(padx=15, pady=(15, 99))

##################
# Window Mainloop

window.after(10, refresh_program)
window.mainloop()
