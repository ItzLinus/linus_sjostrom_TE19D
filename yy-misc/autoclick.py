# add the appJar folder to your PATH
import sys
sys.path.append("E:\PYLIB")
# import the appJar library
from appJar import gui
import pyautogui
import appJar
 
def buttonPress(button):
    if(button == "Go"):
        amount = int(app.getEntry("amount"))
        button = app.radioButton("click")
        if(button == "Right Click"):
            button = "right"
        else:
            button = "left"
        for _ in range(amount):
            pyautogui.click(button=button)
 
app = appJar.gui("autoclicker")
app.setSize("300x200")
app.setSticky("new")
app.addLabel("Enter amount of clicks", row=0)
app.addEntry("amount", row=1)
app.addButton("Go", buttonPress, row=3)
app.setSticky("e")
app.radioButton("click", "Right Click", row=2)
app.setSticky("w")
app.radioButton("click", "Left Click", row=2)
 
app.go()