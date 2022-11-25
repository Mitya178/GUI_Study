import tkinter as tk
import tkinter.filedialog as fd
from tkinter import messagebox
from tkinter import ttk


def add_label():
    global col
    tk.Label(text='New text').grid(row=0, column=col)
    col += 1


def counter():
    global count
    count += 1
    btn3['text'] = f'Счетчик:{count}'


def warning():
    messagebox.showwarning('WARNING!', 'Message warning!')


def select_directory():
    global directory
    directory = fd.askdirectory(title='Открыть папку', initialdir='/')
    if directory:
        directory = directory.replace('/', '\\')
        print(directory)
        direct.insert(0, directory)
        btn_dir_file['state'] = tk.ACTIVE


def select_file():
    types = []
    if file_csv_value.get():
        types.append(("CSV", "*.csv"))
    if file_xlsx_value.get():
        types.append(("Excel", "*.xlsx"))
    if file_xls_value.get():
        types.append(("Excel 97-2003", "*.xls"))
    if len(types) > 1:
        file = fd.askopenfilenames(title='Открыть файл', initialdir=directory, filetypes=types)
    elif len(types) == 1:
        file = fd.askopenfilename(title='Открыть файл', initialdir=directory, filetypes=types)
    else:
        file = 0
    if file:
        print(file)


def file_select_all():
    for check in [file_csv, file_xls, file_xlsx]:
        check.select()


def file_unselect_all():
    for check in [file_csv, file_xls, file_xlsx]:
        check.deselect()


def theme():
    if theme_var.get():
        win.config(bg="Gray")
    else:
        win.config(bg="#F0F0F0")


def list_changed(event):
    messagebox.showwarning(title='Result',
                           message=f'Вы выбрали таблицу {combo.get()}!')


directory = '/'
count = 0
col = 1
win = tk.Tk()
win.title("SupLogGen")
win.geometry('650x450+100+200')
win.iconbitmap(r'icon.ico')

# меню
menu = tk.Menu(win)
new_item = tk.Menu(menu)
new_item.add_command(label='Новый')
new_item.add_separator()
new_item.add_command(label='Изменить')
menu.add_cascade(label='Файл', menu=new_item)
win.config(menu=menu)

tk.Button(text='Add new label', command=add_label).grid(row=0, column=0,
                                                        stick='we', padx=5)
tk.Button(text='Warning', command=warning).grid(row=1, column=0)
btn3 = tk.Button(text='Счетчик', command=counter)
btn3.grid(row=2, column=0)

tk.Label(win, text='Выберите фон:').grid(row=3, column=0)
theme_var = tk.BooleanVar()
tk.Radiobutton(win, text='Светлый', variable=theme_var,
               value=False, command=theme).grid(row=3, column=1)
tk.Radiobutton(win, text='Темный', variable=theme_var,
               value=True, command=theme).grid(row=3, column=2)

btn_direct = tk.Button(text='Выбрать директорию', command=select_directory)
btn_direct.grid(row=6, column=0, stick='we', padx=5)
direct = tk.Entry(win)
direct.grid(row=6, column=1, columnspan=5, stick='wens', pady=4, padx=5)

btn_dir_file = tk.Button(text='Выбрать файл', command=select_file, state=tk.DISABLED)
btn_dir_file.grid(row=7, column=0, stick='we', padx=5)

file_csv_value = tk.BooleanVar()
file_csv_value.set(False)
file_csv = tk.Checkbutton(win, text='Файл CSV',
                          variable=file_csv_value, offvalue=False, onvalue=True)
file_csv.grid(row=7, column=1)

file_xlsx_value = tk.BooleanVar()
file_xlsx_value.set(False)
file_xlsx = tk.Checkbutton(win, text='Файл XLSX',
                           variable=file_xlsx_value, offvalue=False, onvalue=True)
file_xlsx.grid(row=7, column=2)

file_xls_value = tk.BooleanVar()
file_xls_value.set(False)
file_xls = tk.Checkbutton(win, text='Файл XLS', variable=file_xls_value,
                          offvalue=False, onvalue=True)
file_xls.grid(row=7, column=3)
tk.Button(win, text='Выбрать все', command=file_select_all).grid(row=7, column=4, padx=5)
tk.Button(win, text='Снять метки', command=file_unselect_all).grid(row=7, column=5, padx=5)

tk.Label(win, text='Выберите таблицу:').grid(row=8, column=0)
lists = ['LOOP_BOOK', 'IO_LIST']
combo = ttk.Combobox(win, values=lists)
combo.grid(row=8, column=1)
combo.bind('<<ComboboxSelected>>', list_changed)

for i in range(8):
    win.grid_columnconfigure(i, minsize=60)
for i in range(8):
    win.grid_rowconfigure(i, minsize=30)
win.mainloop()
