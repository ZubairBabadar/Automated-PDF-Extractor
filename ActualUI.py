import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from TextExtractorZ import nice 
from tableextractor import table 
from OCRz import img


root = tk.Tk()
file_path = ""

def browse_file():
    
    global file_path
    file_path = filedialog.askopenfilename(title="Select a File", filetypes=[("PDF Files", "*.pdf"), ("All Files", "*.*")])
    
    if file_path:  # If a file is selected
        label.config(text=f"Selected File: {file_path}")

def extract_file():

    if not file_path:
        op.config(text = f"No File Found", fg = "red")
        return
    
    else:
        selected_item = combo_box.get()

        if selected_item == "Extract as Text":
            nice(file_path)
            op.config(text = f'"File Sucessfully Created"', fg = "green")
        elif selected_item == "Extract as CSV":
            table(file_path)
            op.config(text = f'"File Sucessfully Created"', fg = "green")
        elif selected_item == "Extract as Image":
            img(file_path)
            op.config(text = f'"File Sucessfully Created"', fg = "green")
        elif selected_item == "Extract as All":
            nice(file_path)
            table(file_path)
            nice(file_path)
            op.config(text = f'"File Sucessfully Created"', fg = "green")
root.title("Automated PDF Extractor")

# Create a label
label = tk.Label(root, text="Selected Item: ")
label.place(x = 80, y = 50)

bf = tk.Label(root, text="Select File: ")
bf.place(x = 93, y = 105)

button = tk.Button(root, text='Browse File', width=25, command=browse_file)
button.place(x = 200, y = 100)

so = Label(root, text='Select Format:')
so.place(x = 80, y = 199)

# Create a Combobox widget
combo_box = ttk.Combobox(root, values=["Extract as Text", "Extract as CSV", "Extract as Image", "Extract as All"], state= "readonly",width=27)
combo_box.place(x = 200, y = 200)
  

# Set default value
combo_box.set("Extract as Text")

extract_button = tk.Button(root, text='Extract', width=25, command=extract_file)
extract_button.place(x = 200, y = 300)

op = Label(root, text='')
op.place(x = 230, y = 350)

# Bind event to selection
combo_box.bind("<<ComboboxSelected>>", extract_file)
root.geometry("600x400")
root.resizable(False,False)
root.mainloop()