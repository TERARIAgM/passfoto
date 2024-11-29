import random
import time
from playsound import playsound
import threading

# Fungsi untuk memainkan suara
def play_sound():
    # Ganti dengan path ke file audio kamu
    playsound('/storage/emulated/0/Download/ngakak.mp3')

# Fungsi untuk mengacak pesan-pesan alien
def generate_alien_message():
    alien_words = [
        "Zkrk! Blip-blop!", "Xalgar Wqfn?!", "Shkklrrr Zzzt!", 
        "Qxrlg Glurrrp...!", "Vzzrkl Vzq-tzzzz!", "Brrraaak Zlrrk??", 
        "Sqqrtrrpp Zzrraaz!?", "Zzznquk...!"
    ]
    return random.choice(alien_words)

# Fungsi prank utama
def alien_prank():
    print("Mempersiapkan pesan dari makhluk alien...!")
    time.sleep(2)
    for i in range(5):
        print(generate_alien_message())
        time.sleep(random.uniform(0.5, 1.5))  # Delay acak antara pesan
    
    print("\nPesan alien selesai... Menunggu balasan...")
    time.sleep(3)
    print("\nPeringatan: Aliens are coming!")

    # Putar suara sebagai efek
    threading.Thread(target=play_sound).start()

# Mulai prank
alien_prank()
