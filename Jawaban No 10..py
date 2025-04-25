
todo_list = {
    "Belajar Python": "belum",
    "Cuci baju": "selesai"
}

def tampilkan_to_do_list():
    print("\nTo-Do List:")
    for tugas, status in todo_list.items():
        print(f"{tugas} - Status: {status}")

def tambah_tugas():
    tugas = input
    status = input
    todo_list[tugas] = status
    print(f"Tugas '{tugas}{status}'.")

def ubah_status_tugas():
    tampilkan_to_do_list()
    tugas = input("\nMasukkan tugas yang ingin diubah statusnya: ")
    if tugas in todo_list:
        status = input("Masukkan status baru tugas (belum/selesai): ")
        todo_list[tugas] = status
        print(f"Status tugas '{tugas}' telah diperbarui menjadi '{status}'.")
    else:
        print(f"Tugas '{tugas}' tidak ditemukan.")

def main():
    while True:
        print("\nMenu:")
        print("1. Tampilkan To-Do List")
        print("2. Tambah Tugas")
        print("3. Ubah Status Tugas")
        print("4. Keluar")
        
        pilihan = input("Pilih menu (1/2/3/4): ")
        
        if pilihan == "1":
            tampilkan_to_do_list()
        elif pilihan == "2":
            tambah_tugas()
        elif pilihan == "3":
            ubah_status_tugas()
        elif pilihan == "4":
            print("Terima kasih telah menggunakan To-Do List.")
            break
        else:
            print("valid.")

if _name_ == "_main_":
    main()