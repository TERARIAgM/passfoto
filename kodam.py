GNU nano 8.2                         cek_khodam.py
    "Babi Ngepet Si Pemburu Tempe", "Bule Si Penjaga Kerupuk", "Kucing Hideung Si Pencu>
    "Burung Hantu Si Tukang Begadang", "Setan Gendruwo Si Pemilik Tiket Sinetron", "Lab>
    "Cacing Si Penasihat Hirup", "Monyet Si Penggila Gorengan", "Singa Si Nu Nyimpen Ja>
    "Kambing Si Nu Bawa Tawa", "Ular Piton Si Nu Nyusun Puzzle"
]

# Fungsi untuk cek watak acak
def cek_watak(nama):
    chxoosen_watak = random.choice(watak_list)                                                print(f"Watak {nama}: {chosen_watak}")                                                                                                                                      # Fungsi untuk cek khodam acak
def cek_khodam(nama):                                                                       chosen_khodam = random.choice(khodam_list)                                              print(f"Khodam {nama}: {chosen_khodam}")                                            
# Menu utama
def menu():
    while True:
        print("\nPilih menu:")
        print("1. Cek Watak Kamu")
        print("2. Cek Khodam Kamu")
        print("3. Keluar")

        pilihan = input("Masukkan pilihan (1/2/3): ")

        if pilihan == '1':
            nama = input("Masukkan nama orang: ")
            cek_watak(nama)                                                                     elif pilihan == '2':
            nama = input("Masukkan nama orang: ")                                                   cek_khodam(nama)
        elif pilihan == '3':                                                                        print("Terima kasih telah menggunakan program ini!")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

# Jalankan menu
menu()
