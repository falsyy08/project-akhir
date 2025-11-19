import csv, os

# --- Nama file CSV ---
FILE = "data_akun.csv"

# --- Fungsi untuk memuat data akun ---
def muat_data():
    data = {}
    if os.path.exists(FILE):
        with open(FILE, newline="") as f:
            for row in csv.reader(f):
                if len(row) == 3:
                    rek, pin, saldo = row
                    data[rek] = [pin, int(saldo)]
    else:
        data = {"123": ["111", 5000000], "456": ["222", 1500000]}
    return data

# --- Fungsi untuk menyimpan data akun ---
def simpan_data(data):
    with open(FILE, "w", newline="") as f:
        w = csv.writer(f)
        for rek, (pin, saldo) in data.items():
            w.writerow([rek, pin, saldo])

# --- Load data akun dari CSV ---
DATA_AKUN = muat_data()

print("=== SELAMAT DATANG DI ATM SIMULASI ===")

# --- PROSES LOGIN ---
while True:
    rekening = input("Masukkan Nomor Rekening: ")
    pin = input("Masukkan PIN Anda: ")

    if rekening in DATA_AKUN:
        if DATA_AKUN[rekening][0] == pin:
            print("\n✅ Login Berhasil!")
            break
        else:
            print("❌ PIN salah. Coba lagi.")
    else:
        print("❌ Nomor Rekening tidak terdaftar. Coba lagi.")
    print("--------------------")

# --- MENU UTAMA & TRANSAKSI (CRUD Lengkap) ---
while True:
    print("\n=== Menu Utama ===")
    print("1. Cek Saldo")
    print("2. Tarik Uang")
    print("3. Setor Uang")
    print("4. Buat Akun Baru (CREATE)")
    print("5. Tutup Akun (DELETE)")
    print("6. Keluar")
    
    pilihan = input("Pilih menu (1-6): ")

    # 1. CEK SALDO (READ)
    if pilihan == '1':
        saldo = DATA_AKUN[rekening][1]
        print(f"\n💵 SALDO ANDA SAAT INI: Rp {saldo:,}")
        
    # 2. TARIK UANG (UPDATE)
    elif pilihan == '2':
        j = input("Masukkan jumlah penarikan: ")
        if j.isdigit():
            j = int(j)
            if j <= 0:
                print("❌ Jumlah penarikan harus lebih dari nol.")
            elif j > DATA_AKUN[rekening][1]:
                print("❌ Saldo tidak mencukupi.")
            else:
                DATA_AKUN[rekening][1] -= j
                simpan_data(DATA_AKUN)
                print(f"\n✅ Penarikan Rp {j:,} berhasil.")
                print(f"Saldo tersisa: Rp {DATA_AKUN[rekening][1]:,}")
        else:
            print("❌ Input harus berupa angka.")

    # 3. SETOR UANG (UPDATE)
    elif pilihan == '3':
        j = input("Masukkan jumlah setoran: ")
        if j.isdigit():
            j = int(j)
            if j <= 0:
                print("❌ Jumlah setoran harus lebih dari nol.")
            else:
                DATA_AKUN[rekening][1] += j
                simpan_data(DATA_AKUN)
                print(f"\n✅ Setoran Rp {j:,} berhasil.")
                print(f"Saldo saat ini: Rp {DATA_AKUN[rekening][1]:,}")
        else:
            print("❌ Input harus berupa angka.")

    # 4. BUAT AKUN BARU (CREATE)
    elif pilihan == '4':
        print("\n--- PEMBUKAAN REKENING BARU ---")
        rek_baru = input("Masukkan No. Rekening Baru: ")
        if rek_baru in DATA_AKUN:
            print("❌ Rekening sudah terdaftar.")
        else:
            pin_baru = input("Buat PIN (contoh: 4 digit): ")
            saldo_awal = input("Masukkan Saldo Awal: Rp ")
            if saldo_awal.isdigit():
                DATA_AKUN[rek_baru] = [pin_baru, int(saldo_awal)]
                simpan_data(DATA_AKUN)
                print(f"✅ Akun {rek_baru} berhasil dibuat! Saldo awal: Rp {int(saldo_awal):,}")
            else:
                print("❌ Saldo awal harus berupa angka.")

    # 5. TUTUP AKUN (DELETE)
    elif pilihan == '5':
        print("\n--- PENUTUPAN AKUN ---")
        print("Daftar Akun yang Ada:")
        for r in DATA_AKUN: print(f" - {r}")
        target = input("Masukkan No. Rekening yang ingin ditutup: ")
        if target in DATA_AKUN:
            konfirmasi = input(f"Yakin ingin menutup akun {target}? (Ketik 'TUTUP'): ")
            if konfirmasi.upper() == 'TUTUP':
                DATA_AKUN.pop(target)
                simpan_data(DATA_AKUN)
                print(f"✅ Akun {target} berhasil ditutup.")
                if target == rekening:
                    print("Program berakhir karena akun Anda dihapus.")
                    break
            else:
                print("❌ Pembatalan penutupan akun.")
        else:
            print("❌ Rekening tidak ditemukan.")

    # 6. KELUAR
    elif pilihan == '6':
        print("\nTerima kasih. Silakan ambil kartu Anda.")
        simpan_data(DATA_AKUN)
        break

    else:
        print("Pilihan tidak valid.")
