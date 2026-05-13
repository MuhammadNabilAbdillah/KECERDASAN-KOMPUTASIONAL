def main():
    # 1. Menyiapkan Data Mahasiswa (image_38e596.png)
    # Menambahkan 1 data mahasiswa baru sesuai instruksi image_38e538.png
    data_mahasiswa = [
        {"nama": "Andi", "kehadiran": "Tinggi", "tugas": "Lengkap"},
        {"nama": "Budi", "kehadiran": "Rendah", "tugas": "Tidak Lengkap"},
        {"nama": "Citra", "kehadiran": "Tinggi", "tugas": "Tidak Lengkap"},
        {"nama": "Deni", "kehadiran": "Rendah", "tugas": "Lengkap"},
        {"nama": "Eka", "kehadiran": "Tinggi", "tugas": "Lengkap"}  # Data Baru
    ]

    print("="*40)
    print("   LAPORAN PRESENSI MAHASISWA   ")
    print("="*40)

    # 2. Perulangan untuk menampilkan data (image_38e538.png)
    for mhs in data_mahasiswa:
        nama = mhs["nama"]
        kehadiran = mhs["kehadiran"]
        tugas = mhs["tugas"]

        # 3. Logika Decision Tree (IF-ELSE) (image_38e596.png)
        # Menentukan Status Otomatis
        if kehadiran == "Tinggi":
            status = "Aktif"
        else:
            status = "Tidak Aktif"

        # Menentukan Keterangan (image_38e557.png)
        if tugas == "Lengkap" and kehadiran == "Tinggi":
            keterangan = "Mahasiswa Disiplin"
        else:
            keterangan = "-"

        # 4. Fitur Tambahan: Poin Keaktifan (image_38e538.png)
        poin = 100 if status == "Aktif" and tugas == "Lengkap" else 50

        # 5. Output Program sesuai contoh gambar (image_38e557.png)
        print(f"Nama       : {nama}")
        print(f"Kehadiran  : {kehadiran}")
        print(f"Tugas      : {tugas}")
        print(f"Status     : {status}")
        print(f"Keterangan : {keterangan}")
        print(f"Poin Extra : {poin} (Fitur Tambahan)")
        print("-" * 40)

if __name__ == "__main__":
    main()