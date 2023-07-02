import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

window = tk.Tk()
window.configure(bg="grey")
window.geometry("400x400")
window.resizable(False, False)
window.title("I'm Bored")

# frame input
input_frame = ttk.Frame(window)

#penempatan
input_frame.pack(padx=10, pady=10, fill="x", expand=True)

#komponen komponen
# 1.Label nama depan 
nama_depan_label = ttk.Label(input_frame, text="Nama Depan: ")
nama_depan_label.pack(padx=5, fill="x", expand=True)

# 2. Entry nama depan
Nama_depan = tk.StringVar()
nama_depan_label = ttk.Entry(input_frame, textvariable=Nama_depan)
nama_depan_label.pack(padx=10, pady=10, fill="x", expand=True)

# 3.Label nama belakang
nama_belakang_label = ttk.Label(input_frame, text="Nama Belakang: ")
nama_belakang_label.pack(padx=5, fill="x", expand=True)

# 4. Entry nama belakang
Nama_belakang = tk.StringVar()
nama_belakang_label = ttk.Entry(input_frame, textvariable=Nama_belakang)
nama_belakang_label.pack(padx=10, pady=10, fill="x", expand=True)

# 5. Tombol
def click():
      print("Hello " + Nama_depan.get() + " " + Nama_belakang.get())
      nama = f"Hello {Nama_depan.get()} {Nama_belakang.get()}"
      showinfo(title="New pop-up", message=nama)

tombol_click = ttk.Button(input_frame, text="Submit", command=click)
tombol_click.pack(fill="x", expand=True, padx=10, pady=10)

window.mainloop()