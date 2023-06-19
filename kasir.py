def makan():
    global total_makanan
    menu_makan = int(
        input("1. Babi: 35.000\n2. Ayam: 20.000\n3. Sapi: 28.000\n>>> "))
    if menu_makan == 1:
        jumlah_pesanan_makanan = int(input("Mau berapa banyak: "))
        total_makanan = jumlah_pesanan_makanan * 35000
        print(f"Total makanan: {total_makanan}")

    elif menu_makan == 2:
        jumlah_pesanan_makanan = int(input("Mau berapa banyak: "))
        total_makanan = jumlah_pesanan_makanan * 20000
        print(f"Total makanan: {total_makanan}")

    elif menu_makan == 3:
        jumlah_pesanan_makanan = int(input("Mau berapa banyak: "))
        total_makanan = jumlah_pesanan_makanan * 28000
        print(f"Total makanan: {total_makanan}")


def minum():
    global total_minuman
    menu_minum = int(
        input("1. Air: 2.500\n2. Jus: 15.000\n3. Teh: 8.000\n>>>"))
    if menu_minum == 1:
        jumlah_pesanan_minuman = int(input("Mau berapa banyak: "))
        total_minuman = jumlah_pesanan_minuman * 2500
        print(f"Total minuman: {total_minuman}")

    elif menu_minum == 2:
        jumlah_pesanan_minuman = int(input("Mau berapa banyak: "))
        total_minuman = jumlah_pesanan_minuman * 15000
        print(f"Total minuman: {total_minuman}")

    elif menu_minum == 3:
        jumlah_pesanan_minuman = int(input("Mau berapa banyak: "))
        total_minuman = jumlah_pesanan_minuman * 8000
        print(f"Total minuman: {total_minuman}")


makan()
minum()
print("Total: ", total_makanan + total_minuman)
