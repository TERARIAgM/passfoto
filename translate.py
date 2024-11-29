import time
import sys
from googletrans import Translator

# Kode warna ANSI untuk variasi warna di terminal
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def loading_animation():
    # Animasi loading saat menerjemahkan
    print(f"{Colors.OKCYAN}Menghubungkan ke server Google Translate", end="")
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print(f"{Colors.ENDC}")

def translate_text(text, src_lang, dest_lang):
    # Membuat objek Translator
    translator = Translator()

    # Memulai animasi loading
    loading_animation()

    # Menerjemahkan teks
    translated = translator.translate(text, src=src_lang, dest=dest_lang)
    
    # Menampilkan hasil terjemahan dengan warna
    print(f"\n{Colors.OKCYAN}Terjemahan dari '{text}' ({src_lang} ke {dest_lang}):{Colors.ENDC}")
    print(f"{Colors.OKGREEN}->{translated.text}{Colors.ENDC}\n")

def show_menu():
    # Menampilkan menu dengan warna dan efek tebal
    print(f"{Colors.HEADER}{Colors.BOLD}=== Menu Penerjemah ==={Colors.ENDC}")
    print(f"{Colors.OKBLUE}1. Bahasa Indonesia ke Bahasa Inggris{Colors.ENDC}")
    print(f"{Colors.OKBLUE}2. Bahasa Inggris ke Bahasa Indonesia{Colors.ENDC}")
    print(f"{Colors.WARNING}3. Keluar{Colors.ENDC}")

def main():
    print(f"{Colors.BOLD}{Colors.OKCYAN}Selamat datang di Program Penerjemah!{Colors.ENDC}")
    time.sleep(1)

    while True:
        # Menampilkan menu pilihan dengan sedikit delay untuk memberi kesan interaktif
        show_menu()
        
        choice = input(f"\n{Colors.OKGREEN}Pilih opsi (1/2/3): {Colors.ENDC}")
        
        if choice == '1':
            text = input(f"{Colors.OKCYAN}Masukkan teks dalam Bahasa Indonesia: {Colors.ENDC}")
            translate_text(text, 'id', 'en')  # Bahasa Indonesia ke Bahasa Inggris
        elif choice == '2':
            text = input(f"{Colors.OKCYAN}Masukkan teks dalam Bahasa Inggris: {Colors.ENDC}")
            translate_text(text, 'en', 'id')  # Bahasa Inggris ke Bahasa Indonesia
        elif choice == '3':
            print(f"{Colors.WARNING}Terima kasih telah menggunakan program ini. Sampai jumpa!{Colors.ENDC}")
            break  # Keluar dari program
        else:
            print(f"{Colors.FAIL}Opsi tidak valid. Silakan pilih kembali.{Colors.ENDC}")
            time.sleep(1)

if __name__ == "__main__":
    main()
