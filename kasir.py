def menu_makanan():

    global inputbarang1
    global inputjumlah1
    global totalharga1

    print("DIJUAL\n", "(1) soto: 12.000\n", "(2) mie: 8.000\n", "(3) nasi goreng: 15.000\n")
    inputbarang1 = int(input("Masukkan pesanan bedasarkan nomor: "))
    if inputbarang1 == 1:
        inputjumlah1 = int(input("Jumlah: "))
        totalharga1 = inputjumlah1 * 12000
        print(f"Total harga: {totalharga1}")
    elif inputbarang1 == 2:
        inputjumlah1 = int(input("Jumlah: "))
        totalharga1 = inputjumlah1 * 8000
        print(f"Total harga: {totalharga1}")
    elif inputbarang1 == 3:
        inputjumlah1 = int(input("Jumlah: "))
        totalharga1 = inputjumlah1 * 15000
        print(f"Total harga: {totalharga1}")
    else:
        print("Pilihan tidak ada")

def menu_minuman():

    global inputbarang
    global inputjumlah
    global totalharga

    print("DIJUAL\n", "(1) teh: 4.000\n", "(2) air: 3.000\n", "(3) jus: 8.000\n")
    inputbarang = int(input("Masukkan pesanan bedasarkan nomor: "))
    if inputbarang == 1:
        inputjumlah = int(input("Jumlah: "))
        totalharga = inputjumlah * 4000
        print(f"Total harga: {totalharga}")
    elif inputbarang == 2:
        inputjumlah = int(input("Jumlah: "))
        totalharga = inputjumlah * 3000
        print(f"Total harga: {totalharga}")
    elif inputbarang == 3:
        inputjumlah = int(input("Jumlah: "))
        totalharga = inputjumlah * 8000
        print(f"Total harga: {totalharga}")
    else:
        print("Pilihan tidak ada")

menu_makanan()
menu_minuman()

print(f"Total harga yang harus dibayar:", totalharga1 + totalharga)