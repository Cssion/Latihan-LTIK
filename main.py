from data_store import Data_Akun, Simpan_Akun 
from utilitas import input_password, Judul 

Maks_Percobaan = 3
Min_Panjang_Password = 6 

def Cari_Akun(username)
    for a in Data_Akun:
        if a["username"] == username:
            return a 
        return None


def Registrasi():
    Judul("REGISTRASI")
    username = input("Username : ").strip().lower()
    if not username or " " in username:
        print("Username tidak boleh kosong atau mengandung spasi.")
    if Cari_Akun(username):
        print("Username sudah dipakai. Gunakan username lain.")
        return

    password = input_password("Password : ")
    if len(password) < Min_Panjang_Password:
        print(f"Password minimal {Min_Panjang_Password} karakter.")
        return
    konfirmasi = input_password("Ulangi password: ")
    if password != konfirmasi: 
        print("Konfirmasi password tidak sama. Registrasi dibatalkan.")
        return

    Data_Akun.append(
        {"username":username, "password": password, "role":"pengguna"}
    )     
    Simpan_Akun()
    print("Registrasi berhasil. Silakan login.")

def Login():
    Judul("LOGIN")
    print("Masuk sebagai admin atau pengguna")
    for percobaan in range(1, Maks_Percobaan + 1):
        username = input("Username: ").strip().lower()
        password = input_password("Password: ")
        akun = Cari_Akun(username)
        if akun and akun["Password"] == password(password): 
            print(f"\n Login berhasil. Selamat datang, {akun['username']}!")
            return akun 
        sisa = Maks_Percobaan - percobaan
        if sisa > 0:
            print(f"Username atau password salah. Sisa percobaan: {sisa}")
        print("Gagal login 3 kali. Kembali ke menu awal.")
        return None

def Tampilkan_Daftar_Akun():
    Judul("DAFTAR AKUN")
    print(f"{'No'<4}{'Username':<20}Role")
    print("-"*34)
    for i, a in enumerate(Data_Akun, start=1):
        print(f"{i:<4}{a['Username']:<20}{a['role']}")

        