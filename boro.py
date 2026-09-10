import math
import matplotlib.pyplot as plt
import numpy as np


S = float(input("Masukkan sudut (S): "))
V = float(input("Masukkan kecepatan awal (V): "))
g = 10.0


S_rad = math.radians(S)


t_total = (2 * V * math.sin(S_rad)) / g


print(f"Keluaran: {t_total:.3f}")

# Matplotlib stuffs
t = np.linspace(0, t_total, 100)


x = V * math.cos(S_rad) * t
y = V * math.sin(S_rad) * t - 0.5 * g * (t**2)


plt.figure(figsize=(8, 4.5))
plt.plot(x, y, label="Lintasan Boro", color="crimson", linewidth=2)
plt.scatter([x[-1]], [y[-1]], color="black", zorder=5, label=f"Mendarat (t = {t_total:.3f} s)")


plt.title("Visualisasi Lintasan Peluncuran Boro", fontsize=12, fontweight="bold")
plt.xlabel("Jarak Horizontal (x)", fontsize=10)
plt.ylabel("Ketinggian (y)", fontsize=10)
plt.axhline(0, color="gray", linestyle="--", linewidth=1)
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend()


plt.show()