import time
import datetime as da
import numpy as np

now = da.datetime.now()
print ("Current year: %d yr" % now.year)
print ("Current month: %d month" % now.month)
print ("Current day: %d day" % now.day)
print ("Current hour: %d hr" % now.hour)
print ("Current minute: %d min" % now.minute)
print ("Current second: %d s " % now.second)
print ("Current second:", now.second, "s")
print ("Current microsecond: %d" % now.microsecond)
print (now.strftime("%Y-%m-%d %H:%M"))
print (now.isoformat())

start_time = time.time()
time.sleep(1)
elapsed_time = time.time() - start_time
print ("elapsed_time = %d s" %  elapsed_time)

import ctypes  # An included library with Python install.
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title",2)

# Appjar #########################################
from appJar import gui

# create the GUI & set a title
app = gui("Login Form")

# add labels & entries
# in the correct row & column
app.addLabel("userLab", "Username:", 0, 0)
app.addEntry("userEnt", 0, 1)
app.addLabel("passLab", "Password:", 1, 0)
app.addEntry("passEnt", 1, 1)

# function to print out the name of the button pressed
# followed by the contents of the two entry boxes
def press(btnName):
    print(btnName)
    print(app.getEntry("userEnt"))
    print(app.getEntry("passEnt"))
    if btnName == "Cancel":
        app.stop()

    if app.getEntry("userEnt") == "rjarvis":
        if app.getEntry("passEnt") == "abc":
            app.infoBox("Success", "Congratulations, you are logged in!")
        else:
            app.errorBox("Failed login", "Invalid password")
    else:
        app.errorBox("Failed login", "Invalid username")

# changed this line to call a function
app.addButtons(["Submit", "Cancel"], press, colspan=2)


# start the GUI
app.go()


"""
import tkinter as tk

class popupWindow(object):
    def __init__(self,master):
        top=self.top=Toplevel(master)
        self.l=Label(top,text="Hello World")
        self.l.pack()
        self.e=Entry(top)
        self.e.pack()
        self.b=Button(top,text='Ok',command=self.cleanup)
        self.b.pack()
    def cleanup(self):
        self.value=self.e.get()
        self.top.destroy()

class mainWindow(object):
    def __init__(self,master):
        self.master=master
        self.b=Button(master,text="click me!",command=self.popup)
        self.b.pack()
        self.b2=Button(master,text="print value",command=lambda: sys.stdout.write(self.entryValue()+'\n'))
        self.b2.pack()

    def popup(self):
        self.w=popupWindow(self.master)
        self.b["state"] = "disabled"
        self.master.wait_window(self.w.top)
        self.b["state"] = "normal"

    def entryValue(self):
        return self.w.value


if __name__ == "__main__":
    root=tk()
    m=mainWindow(root)
    root.mainloop()
"""
# comment
'''  Styles:
##  0 : OK
##  1 : OK | Cancel
##  2 : Abort | Retry | Ignore
##  3 : Yes | No | Cancel
##  4 : Yes | No
##  5 : Retry | No 
##  6 : Cancel | Try Again | Continue
'''