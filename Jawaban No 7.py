def kategori_usia(usia):
    kategori = {
        range(0, 12): "Anak-anak",
        range(12, 17): "Remaja",
        range(18, 50): "Dewasa",
        range(60, 100): "Lansia"
    }
    
    # Menentukan kategori usia berdasarkan rentang usia
    for rentang, kategori_usia in kategori.items():
        if usia in rentang:
            return kategori_usia

# Input usia
usia = int(input("Masukkan usia: "))

# Menampilkan kategori usia
print(f"Kategori usia: {kategori_usia(usia)}")