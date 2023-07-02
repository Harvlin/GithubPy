import tkinter as tk
from tkinter import ttk

# init
window = tk.Tk()
window.configure(bg="grey")
window.geometry("400x500")
window.resizable(False, False)
window.title("Calculator")

# frame input
input_frame = ttk.Frame(window)
input_frame.pack(padx=10, pady=10, fill="x", expand=True)

# komponen komponen
# 1. Label nomor pertama
nomor_pertama = ttk.Label(input_frame, text="Masukkan angka ke-1: ")
nomor_pertama.pack(expand=True, padx=10, pady=10)
# 2. Entry nomor pertama
nomorPertama = tk.StringVar()
nomor_pertama = ttk.Entry(input_frame, textvariable=nomorPertama)
nomor_pertama.pack(padx=5, expand=True)

# 3. Label nomor kedua
nomor_kedua = ttk.Label(input_frame, text="Masukkan angka ke-2: ")
nomor_kedua.pack(expand=True, padx=10, pady=10)
# 4. Entry nomor kedua
nomorKedua = tk.StringVar()
nomor_kedua = ttk.Entry(input_frame, textvariable=nomorKedua)
nomor_kedua.pack(padx=5, expand=True)

# 5. Operator
operator = ttk.Label(input_frame, text="Masukkan operator: ")
operator.pack(expand=True, padx=10, pady=10)
Operator = tk.StringVar()
operator = ttk.Entry(input_frame, textvariable=Operator)
operator.pack(padx=5, expand=True)


def hitung():
    angka1 = eval(nomorPertama.get())
    angka2 = eval(nomorKedua.get())
    op = Operator.get()
    match op:
            case "+":
                  hasil = angka1 + angka2
            case "-":
                  hasil = angka1 - angka2
            case "*":
                  hasil = angka1 * angka2
            case "/":
                  hasil = angka1 / angka2

    # Tampilkan hasil pada jendela pesan
    pesan = ttk.Label(window, text=f"Hasil: {hasil}")
    pesan.pack(pady=10)
# 6. Tombol Hitung
hitung_button = ttk.Button(input_frame, text="Hitung", command=hitung)
hitung_button.pack(pady=10)

window.mainloop()