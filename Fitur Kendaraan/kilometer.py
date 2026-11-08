
BATAS_SERVIS = 2000          
PERINGATAN_SISA = 200        


MENU = ("Catat perjalanan", "Lihat riwayat", "Cek kilometer", "Keluar")


riwayat = []


# ---------- 4. FUNCTION & PROCEDURE ----------

def tampilkan_menu():
    print("\n=== MENU KILOMETER ===")
    nomor = 1
    for item in MENU:                  # FOR LOOP: ulangi untuk tiap item tuple
        print(str(nomor) + ". " + item)
        nomor = nomor + 1              # OPERATOR: penjumlahan


# FUNCTION: mengembalikan nilai (ada return)
def hitung_jarak(km_awal, km_akhir):
    jarak = km_akhir - km_awal         # OPERATOR: pengurangan
    return jarak


# FUNCTION: mengembalikan sisa km menuju servis berikutnya
def hitung_sisa_servis(odometer):
    sisa = BATAS_SERVIS - (odometer % BATAS_SERVIS)   # OPERATOR: modulus (%)
    return sisa


# PROCEDURE: mencatat perjalanan baru
def catat_perjalanan(data_kendaraan):
    print("\n--- Catat Perjalanan ---")
    tujuan = input("Tujuan perjalanan: ")
    km_input = input("Kilometer odometer sekarang: ")

    # Validasi: isdigit() cek apakah isinya angka semua
    if km_input.isdigit() == False:
        print("Input harus berupa angka!")
        return                          # keluar dari procedure

    km_akhir = int(km_input)            # CASTING: string -> integer
    km_awal = data_kendaraan["odometer"]

    # IF ELSE: km baru harus lebih besar dari km sebelumnya
    if km_akhir > km_awal:
        jarak = hitung_jarak(km_awal, km_akhir)

        # DICTIONARY: 1 perjalanan = 1 dictionary
        catatan = {
            "tujuan": tujuan,
            "km_awal": km_awal,
            "km_akhir": km_akhir,
            "jarak": jarak
        }
        riwayat.append(catatan)                 # masukkan ke list
        data_kendaraan["odometer"] = km_akhir   # update odometer
        print("Tersimpan! Jarak tempuh:", jarak, "km")
    else:
        print("Gagal! Km harus lebih besar dari", km_awal)


# PROCEDURE: menampilkan semua riwayat
def lihat_riwayat():
    print("\n--- Riwayat Perjalanan ---")
    if len(riwayat) == 0:
        print("Belum ada perjalanan tercatat.")
    else:
        nomor = 1
        for catatan in riwayat:         # FOR LOOP: baca tiap dictionary di list
            print(str(nomor) + ". " + catatan["tujuan"]
                  + " | " + str(catatan["km_awal"])
                  + " -> " + str(catatan["km_akhir"])
                  + " | " + str(catatan["jarak"]) + " km")
            nomor += 1


# PROCEDURE: pengecekan kilometer
def cek_kilometer(data_kendaraan):
    print("\n--- Cek Kilometer ---")
    odometer = data_kendaraan["odometer"]
    print("Kendaraan   :", data_kendaraan["nama"])
    print("Odometer    :", odometer, "km")

    total_jarak = 0
    tujuan_unik = set()                 # SET: otomatis menghapus data kembar
    for catatan in riwayat:
        total_jarak += catatan["jarak"]
        tujuan_unik.add(catatan["tujuan"])

    jumlah = len(riwayat)
    print("Jumlah perjalanan :", jumlah)
    print("Total jarak       :", total_jarak, "km")

    if jumlah > 0:
        rata_rata = total_jarak / jumlah        # OPERATOR: pembagian
        print("Rata-rata/trip    :", round(rata_rata, 1), "km")
        print("Tujuan berbeda    :", len(tujuan_unik), "tempat")

    # Cek status servis
    sisa = hitung_sisa_servis(odometer)
    print("Sisa km servis    :", sisa, "km")
    if sisa <= PERINGATAN_SISA:                 # OPERATOR: perbandingan
        print(">> PERINGATAN: Segera servis kendaraan!")
    else:
        print(">> Kondisi aman, belum perlu servis.")


# ---------- 5. PROGRAM UTAMA ----------
print("=== SELAMAT DATANG DI APLIKASI KILOMETER ===")
nama = input("Nama kendaraan: ")

# Pastikan input odometer awal berupa angka (WHILE LOOP: ulangi sampai benar)
odometer_awal = input("Odometer awal (km): ")
while odometer_awal.isdigit() == False:
    print("Harus angka!")
    odometer_awal = input("Odometer awal (km): ")

# DICTIONARY: menyimpan data kendaraan
data_kendaraan = {
    "nama": nama,
    "odometer": int(odometer_awal)      # CASTING: string -> integer
}

# WHILE LOOP: menu terus muncul sampai user pilih Keluar
jalan = True                            
while jalan:
    tampilkan_menu()
    pilihan = input("Pilih menu (1-4): ")

    if pilihan == "1":
        catat_perjalanan(data_kendaraan)
    elif pilihan == "2":
        lihat_riwayat()
    elif pilihan == "3":
        cek_kilometer(data_kendaraan)
    elif pilihan == "4":
        print("Terima kasih, sampai jumpa!")
        jalan = False                   
    else:
        print("Pilihan tidak valid, coba lagi.")