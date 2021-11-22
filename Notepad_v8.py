"""
link to text widget documentation : https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/text-methods.html
Changelog:
    1. Added a modification check flag for New file and open file.
    2. Added a save confirmation to the open file method.
"""

from tkinter import *
from tkinter import filedialog, messagebox
from tkinter import font
from tkinter import TclError
from find import *

from GUI.Notepad.find import *

root = Tk()
root.title("TextPad by Nishmith!")
root.geometry("750x515")

# Set variable for open file name
global open_status_name
open_status_name = False

#Create a variable clipboard and make it global
global clipboard
clipboard = False

# create new_file function
def new_file():
    global open_status_name
    # Check if the file is modified since last saved
    if my_text.edit_modified():
        # Ask whether to save the current file or not
        answer = messagebox.askquestion("SAVE", "Would you like to save the current file?", )
        # print(answer)
        if answer == "yes":
            save_file()
            # Delete prev text
            my_text.delete("1.0", END)
            # Update tile and ststus bar
            root.title("New File - TextPad!")
            status_bar.config(text='New File        ')

            open_status_name = False
        else:
            # Delete prev text
            my_text.delete("1.0", END)
            # Update tile and ststus bar
            root.title("New File - TextPad!")
            status_bar.config(text='New File        ')

            open_status_name = False
    else:
        # Delete prev text
        my_text.delete("1.0", END)
        # Update tile and ststus bar
        root.title("New File - TextPad!")
        status_bar.config(text='New File        ')

        open_status_name = False

# create open_file function
def open_file():
    # Make file name global so that we can access it later
    global open_status_name
    # Check if the file is modified since last saved
    if my_text.edit_modified():
        answer = messagebox.askquestion("SAVE", "Would you like to save the current file?", )
        # print(answer)
        if answer == "yes":
            save_file()
            # Grab Filename
            text_file = filedialog.askopenfilename(
                initialdir="C:/Users/A299743/PycharmProjects/MyProjects/GUI/Notepad/files/",
                title="Open File", filetypes=(
                    ("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*"),))

            if text_file:
                # Delete prev text
                my_text.delete("1.0", END)
                # Adds a undo separator stack
                my_text.edit_separator()


                open_status_name = text_file
                name = text_file
                status_bar.config(text=f"{name}        ")
                name = name.replace("C:/Users/A299743/PycharmProjects/MyProjects/GUI/Notepad/files/", "")
                root.title(f"{name} - TextPad!")

                # Open the file and read the file
                text_file = open(text_file, 'r')
                stuff = text_file.read()
                # Add file to text box
                my_text.insert(END, stuff)
                # close the file
                text_file.close()
        else:
            # Grab Filename
            text_file = filedialog.askopenfilename(
                initialdir="C:/Users/A299743/PycharmProjects/MyProjects/GUI/Notepad/files/",
                title="Open File", filetypes=(
                    ("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*"),))

            if text_file:
                # Delete prev text
                my_text.delete("1.0", END)

                open_status_name = text_file
                name = text_file
                status_bar.config(text=f"{name}        ")
                name = name.replace("C:/Users/A299743/PycharmProjects/MyProjects/GUI/Notepad/files/", "")
                root.title(f"{name} - TextPad!")

                # Open the file and read the file
                text_file = open(text_file, 'r')
                stuff = text_file.read()
                # Add file to text box
                my_text.insert(END, stuff)
                # close the file
                text_file.close()
    else:
        # Grab Filename
        text_file = filedialog.askopenfilename(
            initialdir="C:/Users/A299743/PycharmProjects/MyProjects/GUI/Notepad/files/",
            title="Open File", filetypes=(
                ("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*"),))

        if text_file:
            # Delete prev text
            my_text.delete("1.0", END)

            open_status_name = text_file
            name = text_file
            status_bar.config(text=f"{name}        ")
            name = name.replace("C:/Users/A299743/PycharmProjects/MyProjects/GUI/Notepad/files/", "")
            root.title(f"{name} - TextPad!")

            # Open the file and read the file
            text_file = open(text_file, 'r')
            stuff = text_file.read()
            # Add file to text box
            my_text.insert(END, stuff)
            # close the file
            text_file.close()
# create save_as_file function
def save_as_file():
    text_file = filedialog.asksaveasfilename(defaultextension=".*",
                                             initialdir="C:/Users/A299743/PycharmProjects/MyProjects/GUI/Notepad/files/",
                                             title="Save File", filetypes=(
            ("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*"),))
    if text_file:
        global open_status_name
        open_status_name = text_file
        # Update status bar
        name = text_file
        status_bar.config(text=f"Saved: {name}        ")
        name = name.replace("C:/Users/A299743/PycharmProjects/MyProjects/GUI/Notepad/files/", "")
        root.title(f"{name} - TextPad!")

        # Save the file
        text_file = open(text_file, 'w')
        text_file.write(my_text.get(1.0, END))
        # Close file
        text_file.close()

        # Show a dialogbox to inform user tht the file is saved.
        messagebox.showinfo("Saved Successfully!", f"The file is saved : {open_status_name}")
        # Adds a undo separator stack
        my_text.edit_separator()


# Save_file function
def save_file():
    global open_status_name
    if open_status_name:
        # Save the file
        text_file = open(open_status_name, 'w')
        text_file.write(my_text.get(1.0, END))
        # Close file
        text_file.close()

        # Show a dialogbox to inform user tht the file is saved.
        messagebox.showinfo("Saved Successfully!", f"The file is saved : {open_status_name}")

        status_bar.config(text=f"Saved: {open_status_name}        ")
        # Adds a undo separator stack
        my_text.edit_separator()
    else:
        save_as_file()

# Copy function
def copy_text(e):
    global clipboard
    try:
        if e:
            clipboard = root.clipboard_get()
        if my_text.selection_get():
            clipboard = my_text.selection_get()
            root.clipboard_clear()
            # clipboard = my_text.get('sel.first', 'sel.last')
            root.clipboard_append(clipboard)
    except TclError:
        pass

# Cut function
def cut_text(e):
    global clipboard
    try:
        if e:
            clipboard = root.clipboard_get()
        else:
            if my_text.selection_get():
                start = my_text.index("sel.first")
                end = my_text.index("sel.last")
                clipboard = my_text.selection_get()
                my_text.delete(start, end)
                root.clipboard_clear()
                root.clipboard_append(clipboard)
    except TclError:
        pass

# Paste function
def paste_text(e):
    global clipboard
    if e:
        clipboard = root.clipboard_get()
    else:
        if clipboard:
            my_text.insert("insert", clipboard)

# Bold function
def bolder():
    bold_font = font.Font(my_text, my_text.cget("font"))
    bold_font.configure(weight="bold")

    my_text.tag_configure("bold", font=bold_font)
    try:
        current_tags = my_text.tag_names("sel.first")
        if "bold" in current_tags:
            # remove bold
            my_text.tag_remove("bold", "sel.first", "sel.last")
        else:
            # add bold
            my_text.tag_add("bold", "sel.first", "sel.last")
    except TclError:
        # nothing was selected
        pass


# italics function
def italics():
    italics_font = font.Font(my_text, my_text.cget("font"))
    italics_font.configure(slant="italic")

    my_text.tag_configure("italics(or anything)", font=italics_font)
    try:
        current_tags = my_text.tag_names("sel.first")
        if "italics(or anything)" in current_tags:
            # remove bold
            my_text.tag_remove("italics(or anything)", "sel.first", "sel.last")
        else:
            # add bold
            my_text.tag_add("italics(or anything)", "sel.first", "sel.last")
    except TclError:
        # nothing was selected
        pass

# find function
# print(my_text.search("Hello", 1.0))

# find next func
def find_all(event):
    find2(my_text)

# Quit function
def quits(event):
    selection = messagebox.askyesnocancel("Quit", "Are you sure to exit?")
    try:
        if selection == True:
            root.quit()
    except:
        pass


# Create mainframe
my_frame = Frame(root)
my_frame.pack(pady=5)

# create a scrollbar for the text box
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

# Create text box
my_text = Text(my_frame, width=60, height=20, font=('Helvetica', 16), selectbackground='yellow',
               selectforeground="black", undo=True, yscrollcommand=text_scroll.set)
my_text.pack()

# Configure our scrollbar
text_scroll.config(command=my_text.yview)

# Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Add File menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New (Ctrl+N)", command=new_file)
file_menu.add_command(label="Open (Ctrl+O)", command=open_file)
file_menu.add_command(label="Save (Ctrl+S)", command=save_file)
file_menu.add_command(label="Save As... (Ctrl+Alt+S)", command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Exit (Ctrl+Q)", command=lambda: quits(event=1))

# Add Edit menu
edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut (Ctrl+X)", command=lambda : cut_text(False))
edit_menu.add_command(label="Copy (Ctrl+C)", command=lambda : copy_text(False))
edit_menu.add_command(label="Paste (Ctrl+V)", command=lambda : paste_text(False))
edit_menu.add_command(label="Undo (Ctrl+Z)", command=lambda: my_text.edit_undo())
edit_menu.add_command(label="Redo (Ctrl+Y)", command=lambda: my_text.edit_redo())

# Add Format Menu
format_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Format", menu=format_menu)
format_menu.add_command(label="Bold (Ctrl+B)", command=bolder)
format_menu.add_command(label="Italics (Alt+I)", command=italics)

# Add Options Menu
options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Find All (Alt+F)", command=find_all)


# Add Status bar to the bottom of app
status_bar = Label(root, text="Ready        ", anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=5)


# Keyboard binding
# Open file using Ctrl+O
root.bind("<Control-Key-o>", lambda e: open_file())
root.bind("<Control-Key-O>", lambda e: open_file())

# Create new file using Ctrl+N
root.bind("<Control-Key-n>", lambda e: new_file())
root.bind("<Control-Key-N>", lambda e: new_file())

# save file using Ctrl+S
root.bind("<Control-Key-s>", lambda e: save_file())
root.bind("<Control-Key-S>", lambda e: save_file())

# save as file using Ctrl+alt+S
root.bind("<Control_L><Alt_L><s>", lambda e: save_as_file())
root.bind("<Control_R><Alt_R><s>", lambda e: save_as_file())
root.bind("<Control_L><Alt_L><S>", lambda e: save_as_file())
root.bind("<Control_R><Alt_R><S>", lambda e: save_as_file())

# Bold using Ctrl+B
root.bind("<Control-Key-b>", lambda e: bolder())
root.bind("<Control-Key-B>", lambda e: bolder())

# Bold using Alt+I
root.bind("<Alt_L><i>", lambda e: italics())
root.bind("<Alt_R><i>", lambda e: italics())
root.bind("<Alt_L><I>", lambda e: italics())
root.bind("<Alt_R><I>", lambda e: italics())

# Exit shortcut
root.bind("<Control-Key-q>", quits)
root.bind("<Control-Key-Q>", quits)

root.bind("<Control-Key-x>", cut_text)
root.bind("<Control-Key-c>", copy_text)
root.bind("<Control-Key-v>", paste_text)

root.bind("<Control-f>", find_all)

root.mainloop()
