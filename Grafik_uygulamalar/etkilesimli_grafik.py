import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def grafik_olustur():
    kategoriler = ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs"]
    degerler = [10, 25, 18, 32, 28]

    grafik.clear()
    ax = grafik.add_subplot(111)

    tur = grafik_turu.get()

    if tur == "Çizgi":
        ax.plot(kategoriler, degerler, marker="o")
    elif tur == "Sütun":
        ax.bar(kategoriler, degerler)
    elif tur == "Dağılım":
        ax.scatter(kategoriler, degerler)

    ax.set_title("Satış Grafiği")
    ax.set_xlabel("Ay")
    ax.set_ylabel("Satış")
    ax.grid(True)

    canvas.draw()

    # Başarı mesajı
    mesaj.config(text="Grafik oluşturulmuştur, işlem başarılı!")


# Ana pencere
pencere = tk.Tk()
pencere.title("Etkileşimli Grafik Uygulaması")
pencere.geometry("800x600")


# Grafik türü
tk.Label(pencere, text="Grafik türü:").pack(pady=5)

grafik_turu = ttk.Combobox(
    pencere,
    values=["Çizgi", "Sütun", "Dağılım"],
    state="readonly"
)
grafik_turu.set("Çizgi")
grafik_turu.pack()


# Buton
tk.Button(
    pencere,
    text="Grafiği Oluştur",
    command=grafik_olustur
).pack(pady=10)


# Başarı mesajı
mesaj = tk.Label(
    pencere,
    text="",
    font=("Arial", 11)
)
mesaj.pack(pady=5)


# Matplotlib grafiği
grafik = Figure(figsize=(7, 4), dpi=100)
canvas = FigureCanvasTkAgg(grafik, master=pencere)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)


pencere.mainloop()
