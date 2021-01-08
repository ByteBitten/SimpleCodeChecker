'''
Simple Code Checker
v0.1 (07-01-2021) By Ruben Plugge aka ByteBitten
Python 3.9.1

'''

from tkinter import *
import configparser
import screeninfo

#####

# Load config
config = configparser.ConfigParser()
config.read('config.ini')

#####
# Variables
selectedMonitor = int(config['MAIN']['DisplayMonitor'])
code_check = 0
codeLength = int(config['MAIN']['CodeLength'])

#####
# System

root = Tk()
root.title('Code Verifier')
root.iconbitmap('Assets/icon.ico')
root.bind(config['MAIN']['QuitKey'],lambda e: root.quit())

# Read monitor-specs for multi-monitor
monitors = []
for m in screeninfo.get_monitors():
    monitors.append(['monitor', m.x, m.y, m.width, m.height, m.name])

zerox = int(monitors[selectedMonitor][1])
zeroy = int(monitors[selectedMonitor][2])
monwidth = int(monitors[selectedMonitor][3])
monheight = int(monitors[selectedMonitor][4])

location = "{}x{}+{}+{}".format(monwidth, monheight, zerox, zeroy)

root.geometry(location)
root.overrideredirect(True)

#####
# Functions

# Input limiter function (WIP)
def num_limit(p, this_field):
    global codeLength
    
    if p == "":
        return True
    else:
        print("Entry" + this_field + ": " + p)
    
    this_field = int(this_field)
    
    entries = [entry1, entry2, entry3, entry4, entry5, entry6]
    
    if this_field < codeLength:
        next_field = entries[this_field]
    
    # Check if it's a number
    if p.isdigit():
        if this_field < codeLength:
            # Set focus on next field
            next_field.focus_set()
        else:
            root.after(100, code_checker)
        return True
    else:
        # Check if it's Backspace or del/home/end/PgUp/PgDn
        if p != "\x08" and p != "":
            print("Entry" + this_field + ": " + p)
            return False
        else:
            if this_field < codeLength:
                next_field.focus_set()
            else:
                return True

def code_checker():
    global code_check
    global codeLength
    
    enteredCode = ''
    
    enteredCode += entry1.get()
    enteredCode += entry2.get()
    enteredCode += entry3.get()
    
    if codeLength == 3:
        if enteredCode in config['3codes']['list']:
            code_check = 1
        else:
            code_check = 2
    if codeLength == 4:
        enteredCode += entry4.get()
        if enteredCode in config['4codes']['list']:
            code_check = 1
        else:
            code_check = 2
    if codeLength == 5:
        enteredCode += entry4.get()
        enteredCode += entry5.get()
        if enteredCode in config['5codes']['list']:
            code_check = 1
        else:
            code_check = 2
    if codeLength == 6:
        enteredCode += entry4.get()
        enteredCode += entry5.get()
        enteredCode += entry6.get()
        if enteredCode in config['6codes']['list']:
            code_check = 1
        else:
            code_check = 2
    show_result()

def show_result():
    global code_check
    print("== Show Result ==")
    print(code_check)
    # If code is correct
    if code_check == 1:
        # Image code accepted
        main_canvas.itemconfig(imgbg, image = codeAccepted)
    # If code is wrong
    elif code_check == 2:
        # Image code denied
        main_canvas.itemconfig(imgbg, image = codeDenied)
        
        # Clear fields
        entry1.delete(0, END)
        entry2.delete(0, END)
        entry3.delete(0, END)
        entry4.delete(0, END)
        entry5.delete(0, END)
        entry6.delete(0, END)
        
        # Set focus to first field
        entry1.focus_set()
        
        #main_canvas.after(1000, main_canvas.itemconfig(imgbg, image = background))
        
    else:
        pass

#####
# Screen items

# Load images
background = PhotoImage(file='Assets/background.png')
companyLogo = PhotoImage(file='Assets/company_logo.png')
codeDenied = PhotoImage(file='Assets/redbg.png')
codeAccepted = PhotoImage(file='Assets/greenbg.png')

# Set fullscreen canvas
main_canvas = Canvas(root, bg="#000000", bd=0, highlightthickness=0)
main_canvas.pack(fill="both", expand=True)

width = root.winfo_screenwidth()
height = root.winfo_screenheight()

# Set background image in canvas
imgbg = main_canvas.create_image(monwidth/2, height/2, image=background)
imgbg

# Company logo
imglogo = main_canvas.create_image(monwidth/2, 100, anchor=N, image=companyLogo)
imglogo

# Top text
imgtoptext = main_canvas.create_text(monwidth/2, 375, anchor=N, text=config['TopText']['Text'], font=(config['TopText']['FontType'], config['TopText']['FontSize']), fill=config['TopText']['FontColor'])
imgtoptext

# Input num limiter command
vcmd = root.register(func=num_limit)

# 3-6 single-digit input fields
entry1 = Entry(root, validate='key', validatecommand=(vcmd, '%P', 1), font=(config['EntryFields']['FontType'], config['EntryFields']['FontSize']), fg=config['EntryFields']['FontColor'], bg=config['EntryFields']['BGColor'], width=config['EntryFields']['Width'], bd=0, justify='center')
entry2 = Entry(root, validate='key', validatecommand=(vcmd, '%P', 2), font=(config['EntryFields']['FontType'], config['EntryFields']['FontSize']), fg=config['EntryFields']['FontColor'], bg=config['EntryFields']['BGColor'], width=config['EntryFields']['Width'], bd=0, justify='center')
entry3 = Entry(root, validate='key', validatecommand=(vcmd, '%P', 3), font=(config['EntryFields']['FontType'], config['EntryFields']['FontSize']), fg=config['EntryFields']['FontColor'], bg=config['EntryFields']['BGColor'], width=config['EntryFields']['Width'], bd=0, justify='center')
entry4 = Entry(root, validate='key', validatecommand=(vcmd, '%P', 4), font=(config['EntryFields']['FontType'], config['EntryFields']['FontSize']), fg=config['EntryFields']['FontColor'], bg=config['EntryFields']['BGColor'], width=config['EntryFields']['Width'], bd=0, justify='center')
entry5 = Entry(root, validate='key', validatecommand=(vcmd, '%P', 5), font=(config['EntryFields']['FontType'], config['EntryFields']['FontSize']), fg=config['EntryFields']['FontColor'], bg=config['EntryFields']['BGColor'], width=config['EntryFields']['Width'], bd=0, justify='center')
entry6 = Entry(root, validate='key', validatecommand=(vcmd, '%P', 6), font=(config['EntryFields']['FontType'], config['EntryFields']['FontSize']), fg=config['EntryFields']['FontColor'], bg=config['EntryFields']['BGColor'], width=config['EntryFields']['Width'], bd=0, justify='center')

# Entry position adjust
field1 = -200
field2 = 0
field3 = 200
field4 = 300
field5 = 400
field6 = 500

# Entry placing
if int(codeLength) == 3:
    entry_window1 = main_canvas.create_window(monwidth/2+field1, 500, anchor=N, window=entry1)
    entry_window2 = main_canvas.create_window(monwidth/2+field2, 500, anchor=N, window=entry2)
    entry_window3 = main_canvas.create_window(monwidth/2+field3, 500, anchor=N, window=entry3)
elif int(codeLength) == 4:
    field1 = field1-100
    field2 = field2-100
    field3 = field3-100
    entry_window1 = main_canvas.create_window(monwidth/2+field1, 500, anchor=N, window=entry1)
    entry_window2 = main_canvas.create_window(monwidth/2+field2, 500, anchor=N, window=entry2)
    entry_window3 = main_canvas.create_window(monwidth/2+field3, 500, anchor=N, window=entry3)
    entry_window4 = main_canvas.create_window(monwidth/2+field4, 500, anchor=N, window=entry4)
elif int(codeLength) == 5:
    field1 = field1-200
    field2 = field2-200
    field3 = field3-200
    field4 = field4-100
    entry_window1 = main_canvas.create_window(monwidth/2+field1, 500, anchor=N, window=entry1)
    entry_window2 = main_canvas.create_window(monwidth/2+field2, 500, anchor=N, window=entry2)
    entry_window3 = main_canvas.create_window(monwidth/2+field3, 500, anchor=N, window=entry3)
    entry_window4 = main_canvas.create_window(monwidth/2+field4, 500, anchor=N, window=entry4)
    entry_window5 = main_canvas.create_window(monwidth/2+field5, 500, anchor=N, window=entry5)
elif int(codeLength) == 6:
    field1 = field1-300
    field2 = field2-300
    field3 = field3-300
    field4 = field4-200
    field5 = field5-100
    entry_window1 = main_canvas.create_window(monwidth/2+field1, 500, anchor=N, window=entry1)
    entry_window2 = main_canvas.create_window(monwidth/2+field2, 500, anchor=N, window=entry2)
    entry_window3 = main_canvas.create_window(monwidth/2+field3, 500, anchor=N, window=entry3)
    entry_window4 = main_canvas.create_window(monwidth/2+field4, 500, anchor=N, window=entry4)
    entry_window5 = main_canvas.create_window(monwidth/2+field5, 500, anchor=N, window=entry5)
    entry_window6 = main_canvas.create_window(monwidth/2+field6, 500, anchor=N, window=entry6)
else:
    pass

entry1.focus_set()

# Instructions text
main_canvas.create_text(monwidth/2, 700, anchor=N, text=config['InstructionText']['Text'], font=(config['InstructionText']['FontType'], config['InstructionText']['FontSize']), fill=config['InstructionText']['FontColor'])

# Bottom text
main_canvas.create_text(monwidth/2, 1025, anchor=N, text=config['BottomText']['Text'], font=(config['BottomText']['FontType'], config['BottomText']['FontSize']), fill=config['BottomText']['FontColor'])

#####

root.mainloop()
