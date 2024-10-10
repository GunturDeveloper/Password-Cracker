import random
import os
import time

print("Simulasi Brute Force Sederhana By GunturDeveloper")
u_pwd = input("Masukkan password anda: ")

pwd = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
       'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 
       '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '@', '#', '$', '&', '-', '+', ',']

found_password = []
start_time = time.time()

for i in range(len(u_pwd)):
    found = False
    while not found:
        guess = pwd[random.randint(0, len(pwd) - 1)]
        if guess == u_pwd[i]:
            found_password.append(guess)
            found = True
            print(f"Karakter ditemukan: {guess}")
            print("Sedang mencari karakter selanjutnya...")
            os.system('cls' if os.name == 'nt' else 'clear')

end_time = time.time()

time_taken = end_time - start_time
minutes, seconds = divmod(time_taken, 60)
milliseconds = (seconds - int(seconds)) * 1000

print("Password ditemukan: ", ''.join(found_password))
print(f"Waktu yang dibutuhkan: {int(minutes)} menit {int(seconds)} detik {int(milliseconds)} milidetik")
