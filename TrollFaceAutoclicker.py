import pyautogui
import time
import tkinter as tk
from tkinter import ttk 
import threading
import keyboard
clickIndicator=False
mdL=False
mdR=False
def toggleClickin(event=None):
    global clickIndicator
    global mdL
    global mdR
    clickIndicator=not clickIndicator
    updateStatus()
    if mdL:
        pyautogui.mouseUp(button="left")
        mdL=False
    if mdR:
        pyautogui.mouseUp(button="right")
        mdR=False
    keyboard.release(keyVar.get())
def looper():
    global mdL
    global mdR
    while True:
        if clickIndicator and not isMouseInWindow():
            action=clickType.get()
            if CorH.get()== "click":
                if action=="leftClick":
                    pyautogui.click(button="left")
                elif action=="rightClick":
                    pyautogui.click(button="right")
                elif action=="key":
                    keyboard.press(keyVar.get())
                    keyboard.release(keyVar.get())
                time.sleep(getDelay())
            else:
                if action=="leftClick":
                    pyautogui.mouseUp(button="left")
                    time.sleep(0.1)
                    pyautogui.mouseDown(button="left")
                    mdL = True
                elif action=="rightClick":
                    pyautogui.mouseUp(button="right")
                    time.sleep(0.1)
                    pyautogui.mouseDown(button="right")
                    mdR = True
                elif action=="key":
                    keyboard.release(keyVar.get())
                    time.sleep(0.1)
                    keyboard.press(keyVar.get())
                time.sleep(getDuration())
        else:
            time.sleep(0.01)
def validateFloat(text):
    if text=="":
        return True
    try:
        float(text)
        return True
    except:
        return False
def isMouseInWindow():
    x, y = pyautogui.position()
    win_x = root.winfo_rootx()
    win_y = root.winfo_rooty()
    win_w = root.winfo_width()
    win_h = root.winfo_height()
    return (win_x <= x <= win_x + win_w and win_y <= y <= win_y + win_h)
def getDelay():
    try:
        value=float(delayEntry.get())
        if value<0.01:
            value=0.01
        if value>5:
            value=5
        delayEntry.delete(0,tk.END)
        delayEntry.insert(0,str(value))
        return value
    except:
        delayEntry.delete(0,tk.END)
        delayEntry.insert(0,"0.1")
        return 0.1
def getDuration():
    try:
        value=float(holdEntry.get())
        if value<0.5:
            value=0.5
        if value>60:
            value=60
        holdEntry.delete(0,tk.END)
        holdEntry.insert(0,str(value))
        return value
    except:
        holdEntry.delete(0,tk.END)
        holdEntry.insert(0,"5")
        return 5
def changeCorH():
    if CorH.get() == "click":
        entryLabel.config(text="delay (secs):")
        holdEntry.grid_remove()
        delayEntry.grid()
    else:
        entryLabel.config(text="duration (secs):")
        delayEntry.grid_remove()
        holdEntry.grid()
def updateStatus():
    if clickIndicator:
        button.config(text="stop dat shit")
        statusLabel.config(text="Status: ACTIVE",fg="green")
    else:
        button.config(text="start da clickin'")
        statusLabel.config(text="Status: INACTIVE",fg="red")
def updateKeyMenu(*args):
    if clickType.get()=="key":
        keyMenu.grid()
    else:
        keyMenu.grid_remove()
root=tk.Tk()
root.title("TrollFaceAutoclicker")
root.iconbitmap("trollface.ico")
root.geometry("400x350")
root.configure(bg="#1e1e1e")
root.resizable(False,False)
def blockFullscreen(event):
    return "break"
root.bind("<F11>",blockFullscreen)
root.bind("<Alt-Return>",blockFullscreen)
clickType=tk.StringVar(value="leftClick")
keyVar=tk.StringVar(value="space")
CorH=tk.StringVar(value="click")
style = ttk.Style()
style.theme_use("default")
style.configure("Dark.TCombobox",fieldbackground="#2a2a2a",background="#2d2d2d",foreground="white",arrowcolor="white")
style.map("Dark.TCombobox",fieldbackground=[("readonly", "#2a2a2a")],foreground=[("readonly", "white")])
title=tk.Label(root,text="TrollFaceAutoclicker",font=("Segoe UI",20,"bold"),bg="#1e1e1e",fg="blue")
title.pack(pady=5)
author=tk.Label(root,text="made by N0F4C3 a.k.a Bo",font=("Segoe UI",7),bg="#1e1e1e",fg="gray")
author.pack(pady=2.5)
info=tk.Label(root,text="Press F6 to start/stop",font=("Segoe UI",10),bg="#1e1e1e",fg="white")
info.pack(pady=5)
statusLabel=tk.Label(root,text="Status: INACTIVE",font=("Segoe UI",15),bg="#1e1e1e",fg="red")
statusLabel.pack(pady=10)
button=tk.Button(root,text="start da clickin'",command=toggleClickin,bg="#2d2d2d",fg="white",activebackground="#444",activeforeground="white")
button.pack(pady=10)
frame3=tk.Frame(root,bg="#1e1e1e")
frame3.place(relx=0.5,rely=0.65, anchor="center")
click=tk.Radiobutton(frame3, text="click", variable=CorH, value="click",command=changeCorH)
click.grid(row=0,column=0,padx=5)
hold=tk.Radiobutton(frame3, text="hold", variable=CorH, value="hold",command=changeCorH) #CorH = Click or Hold
hold.grid(row=0,column=1,padx=5)
frame=tk.Frame(root,bg="#1e1e1e")
frame.place(relx=0.5,rely=0.75,anchor="center")
entryLabel=tk.Label(frame,text="Delay (secs):",bg="#1e1e1e",fg="white")
entryLabel.grid(row=0,column=0,padx=5)
validate=(root.register(validateFloat),"%P")
delayEntry=tk.Entry(frame,width=5,validate="key",validatecommand=validate,bg="#2a2a2a",fg="white",insertbackground="white")
delayEntry.insert(0,"0.1")
delayEntry.grid(row=0,column=1,padx=5)
holdEntry=tk.Entry(frame,width=5,validate="key",validatecommand=validate,bg="#2a2a2a",fg="white",insertbackground="white")
holdEntry.insert(0,"5")
holdEntry.grid(row=0,column=1,padx=5)
frame2=tk.Frame(root,bg="#1e1e1e")
frame2.place(relx=0.5,rely=0.85,anchor="center")
actionMenu=tk.OptionMenu(frame2,clickType,"leftClick","rightClick","key")
actionMenu.config(bg="#2d2d2d",fg="white")
actionMenu.grid(row=0,column=0,padx=5)
keys=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","space","enter","shift","ctrl","alt","tab","esc","up","down","left","right","f1","f2","f3","f4","f5","f6","f7","f8","f9","f10","f11","f12"]
keyMenu = ttk.Combobox(frame2, textvariable=keyVar, values=keys, state="readonly", width=10, style="Dark.TCombobox")
keyMenu.grid(row=0,column=1,padx=5)
keyMenu.current(0)
clickType.trace_add("write",updateKeyMenu)
updateKeyMenu()
changeCorH()
keyboard.add_hotkey("F6",toggleClickin)
thread=threading.Thread(target=looper)
thread.daemon=True
thread.start()
root.mainloop()
