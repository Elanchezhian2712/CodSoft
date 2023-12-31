import tkinter as tk
from tkinter import messagebox
from tkinter import font
from PIL import Image, ImageTk

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    selected_index = task_listbox.curselection() 
    if selected_index:
        task_listbox.delete(selected_index)

def edit_task():
    selected_index = task_listbox.curselection()
    if selected_index:
        edited_task = task_entry.get()
        if edited_task:
            task_listbox.delete(selected_index)
            task_listbox.insert(selected_index, edited_task)
            task_entry.delete(0, tk.END)

def clear_tasks():
    task_listbox.delete(0, tk.END)

# Create the main application window
root = tk.Tk()
root.title("To-Do List App")

# Calculate the center coordinates of the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 600
window_height = 600

x_coordinate = (screen_width - window_width) // 2
y_coordinate = (screen_height - window_height) // 2

# Set the window's position
root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

root.configure(bg="#34495e")  # Set background color

pil_image = Image.open("code.jpg")  # Replace with your image file
image = ImageTk.PhotoImage(pil_image)
image_label = tk.Label(root, image=image, bg="#34495e")
image_label.pack(pady=20)

# Create a custom font object using "Helvetica Neue"
custom_font = font.Font(family="Helvetica Neue", size=14)

# Entry widget to input tasks
task_entry = tk.Entry(root, font=custom_font, bg="#ecf0f1", fg="#34495e", justify='center')
task_entry.pack(padx=40, pady=(0, 20), fill=tk.X)

# Buttons with modern styling
button_styles = {
    "font": custom_font,
    "bg": "#3498db",  # Blue
    "fg": "white",
    "activebackground": "#2980b9",
    "activeforeground": "white",
    "bd": 0,
    "relief": tk.FLAT,
    "width": 15,
}

add_button = tk.Button(root, text="Add Task", command=add_task, **button_styles)
add_button.pack(padx=40, pady=10, fill=tk.X)

edit_button = tk.Button(root, text="Edit Task", command=edit_task, **button_styles)
edit_button.pack(padx=40, pady=5, fill=tk.X)

delete_button = tk.Button(root, text="Delete Task", command=delete_task, **button_styles)
delete_button.pack(padx=40, pady=5, fill=tk.X)

clear_button = tk.Button(root, text="Clear All Tasks", command=clear_tasks, **button_styles)
clear_button.pack(padx=40, pady=5, fill=tk.X)

# Listbox with modern styling
listbox_styles = {
    "font": custom_font,
    "bg": "#ecf0f1",
    "fg": "#34495e",
    "selectbackground": "#2980b9",
    "selectforeground": "white",
    "activestyle": "none",
}
task_listbox = tk.Listbox(root, **listbox_styles)
task_listbox.pack(padx=40, pady=20, fill=tk.BOTH, expand=True)

root.mainloop()
