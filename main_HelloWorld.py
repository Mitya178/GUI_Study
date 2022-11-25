import tkinter as tk

# Tkinter Window
root_window = tk.Tk()

# Window Settings
root_window.title('GUI_HELLO_WORLD')
root_window.geometry('300x100')
root_window.configure(background = '#353535')

# Text
tk.Label(root_window, text='Hello World', fg='Red', bg='#353535').pack()

# Exit Button
tk.Button(root_window, text='Exit', width=10, command=root_window.destroy).pack()

# Main loop
root_window.mainloop()
