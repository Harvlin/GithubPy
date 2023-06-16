def hitung_imc(berat, tinggi):
      imc = berat / (tinggi * tinggi)
      return imc
def kategori(imc):
      if imc < 18.5:
            return "Kurus"
      elif imc < 25:
            return "Normal"
      elif imc < 30:
            return "Berat berlebih"
      else:
            return "Obesitas"
      
berat = eval(input("Masukkan berat badan (kg): "))
tinggi = eval(input("Masukkan tinggi (m): "))
imc = hitung_imc(berat, tinggi)
kategori_imc = kategori(imc)

print("IMC: ", imc)
print("Kategori", kategori_imc)