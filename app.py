import random
import os
print("Guntur Cracker")
u_pwd = input("Masukkan password anda :  ")

pwd = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
       'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 
       '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

pw = ""
while pw != u_pwd:
    pw = ""
    for letter in range(len(u_pwd)):
        guess_pwd = pwd[random.randint(0, len(pwd)-1)]
        pw = str(pw) + str(guess_pwd)
    print(pw)
    print("Sedang mencari password...")
    os.system('cls' if os.name == 'nt' else 'clear')

print("Password ditemukan : ", pw)
