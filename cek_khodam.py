import random

# Daftar watak seseorang yang lucu dan ngakak
watak_list = [
    "Si Tukang Ngomong Terus", "Si Pemalu Tapi Kocak", "Si Suka Nganggu Temen Tidur",
    "Si Penikmat Makan Tapi Malas Masak", "Si Suka Ngegosip", "Si Rajin Tapi Suka Lupa", 
    "Si Penggila Drama", "Si Pembuat Keributan", "Si Pelupa Tapi Terus Ngedumel",
    "Si Tukang Ketawa Sendiri", "Si Pendiam Tapi Suka Ngeprank", "Si Suka Ngerjain Orang",
    "Si Suka Ngarecokin Temen Tapi Baik Hati", "Si Pemalu Yang Tiba-tiba Berani", "Si Tukang Selfie Tanpa Henti",
    "Si Suka Nanyain Hal Yang Sama", "Si Suka Curhat Tapi Gak Dengerin Orang", "Si Tukang Baper",
    "Si Ratu Drama Tapi Manja", "Si Pemburu Wi-Fi Gratis"
]

# Daftar nama khodam lucu
khodam_list = [
    "Setan Si Kukusan", "Hantu Si Hayam Ceker", "Pocong Si Kaki Tilu",
    "Iblis Si Pambawa Mie Goreng", "Kuntilanak Si Nu Suka Cemberut", "Genderuwo Si Pencuri Roti",
    "Lele Si Tukang Ngomongkeun Jalma", "Buto Ijo Si Panghuni Kulkas", "Tikus Si Ahli Dahar Keju",
    "Babi Ngepet Si Pemburu Tempe", "Bule Si Penjaga Kerupuk", "Kucing Hideung Si Pencuri Kadaharan",
    "Burung Hantu Si Tukang Begadang", "Setan Gendruwo Si Pemilik Tiket Sinetron", "Laba-laba Si Pembuat Jaring",
    "Cacing Si Penasihat Hirup", "Monyet Si Penggila Gorengan", "Singa Si Nu Nyimpen Jagung Rebus",
    "Kambing Si Nu Bawa Tawa", "Ular Piton Si Nu Nyusun Puzzle"
]

# Fungsi untuk cek watak acak
def cek_watak(nama):
    chosen_watak = random.choice(watak_list)
    print(f"Watak {nama}: {chosen_watak}")

# Fungsi untuk cek khodam acak
def cek_khodam(nama):
    chosen_khodam = random.choice(khodam_list)
    print(f"Khodam {nama}: {chosen_khodam}")

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
            cek_watak(nama)
        elif pilihan == '2':
            nama = input("Masukkan nama orang: ")
            cek_khodam(nama)
        elif pilihan == '3':
            print("Terima kasih telah menggunakan program ini!")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

# Jalankan menu
menu()
