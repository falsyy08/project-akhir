# ===== Program ATM Sederhana =====

# Saldo awal dan PIN
saldo = 1000000
pin_asli = "1234"

# Kesempatan salah PIN
kesempatan = 3

# --- Tahap Login ---
print("===== Selamat datang di ATM BuluKumba =====")
while kesempatan > 0:
    pin = input("Masukkan PIN Anda: ")

    if pin == pin_asli:
        print("Login berhasil!")
        break
    else:
        kesempatan -= 1
        print(f"PIN salah! Kesempatan tersisa: {kesempatan}")

        if kesempatan == 0:
            print("Akun terblokir. Silakan hubungi bank.")
            exit()

# --- Menu Utama ---
while True:
    print("===== MENU ATM =====")
    print("1. Cek Saldo")
    print("2. Tarik Uang")
    print("3. Setor Uang")
    print("4. Keluar")

    pilihan = input("Pilih menu (1/2/3/4): ")

    # Cek Saldo
    if pilihan == "1":
        print(f"Saldo Anda saat ini: Rp {saldo:,}")

    # Tarik Uang
    elif pilihan == "2":
        tarik = int(input("Masukkan jumlah penarikan: Rp "))
        if tarik <= saldo:
            saldo -= tarik
            print(f"Penarikan berhasil. Sisa saldo: Rp {saldo:,}")
        else:
            print("Saldo tidak cukup!")

    # Setor Uang
    elif pilihan == "3":
        setor = int(input("Masukkan jumlah setoran: Rp "))
        saldo += setor
        print(f"Setoran berhasil. Saldo sekarang: Rp {saldo:,}")

    # Keluar
    elif pilihan == "4":
        print("Terima kasih telah menggunakan ATM ini 🙌")
        break

    # Pilihan tidak valid
    else:
        print("Pilihan tidak valid! Silakan pilih menu 1-4.")