
import csv
import os

NAMA_FILE = "kendaraan.csv"


def buat_file():
    if not os.path.exists(NAMA_FILE):
        with open(NAMA_FILE, "w", newline="") as file:
            kolom = [
                "id", "username", "pemilik", "merek", "tipe",
                "jenis", "tahun", "nomor_polisi", "km",
                "km_ganti_terakhir", "tanggal_ganti_terakhir",
                "oli_terakhir", "interval_km", "interval_hari",
                "id_katalog", "km_diperbarui"
            ]

            writer = csv.DictWriter(file, fieldnames=kolom)
            writer.writeheader()



def tambah_kendaraan(username):
    buat_file()

    print("\n=== TAMBAH DATA KENDARAAN ===")

    pemilik = input("Nama pemilik: ")
    merek = input("Merek kendaraan: ")
    tipe = input("Tipe kendaraan: ")
    jenis = input("Jenis kendaraan: ")
    tahun = input("Tahun kendaraan: ")
    nomor_polisi = input("Nomor polisi: ")
    km = input("Kilometer saat ini: ")

    with open(NAMA_FILE, "r", newline="") as file:
        reader = list(csv.DictReader(file))
        id_baru = len(reader) + 1

    data = {
        "id": id_baru,
        "username": username,
        "pemilik": pemilik,
        "merek": merek,
        "tipe": tipe,
        "jenis": jenis,
        "tahun": tahun,
        "nomor_polisi": nomor_polisi,
        "km": km,
        "km_ganti_terakhir": "",
        "tanggal_ganti_terakhir": "",
        "oli_terakhir": "",
        "interval_km": "",
        "interval_hari": "",
        "id_katalog": "",
        "km_diperbarui": ""
    }

    with open(NAMA_FILE, "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=data.keys())
        writer.writerow(data)

    print("Data kendaraan berhasil disimpan.")



def lihat_kendaraan(username):
    buat_file()

    print("\n=== DATA KENDARAAN ===")

    with open(NAMA_FILE, "r", newline="") as file:
        reader = csv.DictReader(file)
        ditemukan = False

        for data in reader:
            if data["username"] == username:
                ditemukan = True

                print("\nID:", data["id"])
                print("Pemilik:", data["pemilik"])
                print("Merek:", data["merek"])
                print("Tipe:", data["tipe"])
                print("Jenis:", data["jenis"])
                print("Tahun:", data["tahun"])
                print("Nomor Polisi:", data["nomor_polisi"])
                print("Kilometer:", data["km"])

        if not ditemukan:
            print("Belum ada data kendaraan.")

if __name__ == "__main__":
    username = input("Masukkan username: ")

    print("\n1. Tambah Kendaraan")
    print("2. Lihat Kendaraan")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_kendaraan(username)
    elif pilihan == "2":
        lihat_kendaraan(username)
    else:
        print("Pilihan tidak tersedia.")