# List transaksi dalam bentuk tuple (jumlah uang, hari)
transaksi = [
    (10000, "Senin"),
    (0, "Selasa"),
    (-5000, "Rabu"),
    (0, "Kamis"),
    (100000, "Jumat"),
    (-20000, "Sabtu"),
    (0, "Minggu")
]

# Daftar hari dalam seminggu
hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]

saldo_akhir = sum(t[0] for t in transaksi)

pengeluaran_terbesar = min(t[0] for t in transaksi if t[0] < 0)  # Pengeluaran (nilai negatif)
hari_pengeluaran_terbesar = next(t[1] for t in transaksi if t[0] == pengeluaran_terbesar)

# 3. Menampilkan hari tanpa transaksi
# Mencari hari yang tidak memiliki transaksi (saldo 0)
hari_tanpa_transaksi = [t[1] for t in transaksi if t[0] == 0]

# Output
print(f"Saldo akhir: {saldo_akhir}")
print(f"Hari pengeluaran terbesar: {hari_pengeluaran_terbesar}")
print(f"Hari tanpa transaksi: {', '.join(hari_tanpa_transaksi)}")