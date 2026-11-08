# menus/main_menu.py
# FUNGSI : Menu awal program: Login, Registrasi, Keluar.
# TUGAS  : Setelah login berhasil, arahkan ke UserMenu atau AdminMenu
#          sesuai role.

#=====NOTE=======
# Setiap user harus memiliki role yang berbeda yaitu User Biasa & admin
# Agar dapat membedakan mana yang masuk ke menu admin dan mana yang masuk ke menu user
# Belum ada nambahin fitur kayak gitu disini
# Baru nambahin validasi akun dan file csv usernya aja


from Utilitas.Judul import Judul
from getpass import getpass
from Utilitas.cek_akun import cek_akun
from Utilitas.Rapihkan_Text import text
import csv
import os

direktori_sekarang = os.path.dirname(__file__)
CSV_FILE = os.path.join(direktori_sekarang,'..','data','akun.csv')



def login():
    max_percobaan = 3

    while max_percobaan > 0:
        Judul("Login Page")
        name = text(input("Masukan nama dari pengguna: "))
        username = text(input("Masukkan Username: "))
        password = getpass("Masukkan Password: ")

        if not username and not password and not name:
            max_percobaan -= 1
            print("field tidak boleh kosong!")
            continue

        user = cek_akun(username)

        if user is not None and user['password'] == password:
            return user          # kembalikan data user agar bisa dipakai menu lain

        max_percobaan -= 1
        print(f"Username atau password salah! Sisa percobaan: {max_percobaan}")

    print("Anda tidak bisa melakukan login lagi")
    return None

