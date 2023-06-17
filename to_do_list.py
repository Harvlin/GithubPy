def tambah_tugas(daftar_tugas, tugas):
      daftar_tugas.append(tugas)
      print("Tugas telah ditambahkan")

def lihat_tugas(daftar_tugas):
      if not daftar_tugas:
            print("Daftar kosong")
      else:
            print("Daftar tugas: ")
            for index, i in enumerate(daftar_tugas, start=1):
                  print(f"{index}. {i}")
def hapus_tugas(daftar_tugas, nomor_tugas):
      if nomor_tugas < 1 or nomor_tugas > len(daftar_tugas):
            print("Nomor tidak valid")
      else:
            daftar_tugas.pop(nomor_tugas-1)
            print("Tugas: ", nomor_tugas, " Telah dihapus")
      

daftar_tugas = []
while(True):
      pilihan = eval(input("\n--- Aplikasi Daftar Tugas ---\n1. Tambah tugas\n2. Lihat tugas\n3. Hapus tugas\n4. Stop\nPilih menu (1/2/3/4): "))
      if pilihan == 1:
            tambahan_tugas = input("Masukkan tugas baru: ")
            tambah_tugas(daftar_tugas, tambahan_tugas)
      elif pilihan == 2:
            lihat_tugas(daftar_tugas)
      elif pilihan == 3:
            hapustugas = int(input("Masukkan nommor tugas yang ingin dihapus: "))
            hapus_tugas(daftar_tugas, hapus_tugas)
      elif pilihan == 4:
            break
      else:
            raise Exception("Invalid input")
