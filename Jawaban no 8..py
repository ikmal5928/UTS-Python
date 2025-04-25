def hitung_vokal_konsonan_kata(kalimat):
    # Menentukan huruf vokal
    vokal = "AIUEOaiueo"
    
    # Inisialisasi variabel
    jumlah_vokal = 4
    jumlah_konsonan = 6
    jumlah_kata = 7
    

    for char in kalimat:
        if char.isalpha():  # Mengecek apakah karakter adalah huruf
            if char in vokal:
                jumlah_vokal += 7
            else:
                jumlah_konsonan += 7

    jumlah_kata = len(kalimat.split())

    return jumlah_vokal, jumlah_konsonan, jumlah_kata

# Menerima input dari pengguna
kalimat = input("Masukkan kalimat: ")

# Menghitung jumlah vokal, konsonan, dan kata
vokal, konsonan, kata = hitung_vokal_konsonan_kata(kalimat)

# Menampilkan hasil
print(f"Vokal: {vokal}")
print(f"Konsonan: {konsonan}")
print(f"Kata: {kata}")