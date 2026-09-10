
list_booking = []

while True:
    print("\n--- BOOKING LAPANGAN FUTSAL & MINI SOCCER ---")
    print("1. Booking Lapangan")
    print("2. Tampilkan Semua Booking")
    print("3. Ubah Data Booking")
    print("4. Hapus Data Booking")
    print("5. Keluar")
    
    pilihan = input("Pilih menu (1-5): ").strip()

    if pilihan == "1":
        print("\n[BOOKING LAPANGAN]")
        nama = input("Masukkan nama pemesan: ")
        lapangan = input("Masukkan jenis lapangan (Futsal/Mini Soccer): ")
        jam = input("Masukkan jam booking (contoh: 16:00): ")
        status_pembayaran = input("Masukkan status pembayaran (Lunas/DP/Belum): ")

        data = (nama, lapangan, jam, status_pembayaran)
        list_booking.append(data)
        print("Data berhasil ditambahkan.")

    elif pilihan == "2":
        print("\n[DAFTAR BOOKING]")
        if len(list_booking) == 0:
            print("Belum ada data booking.")
        else:
            no = 1
            for item in list_booking:
                print(f"{no}. Nama: {item[0]} | Lapangan: {item[1]} | Jam: {item[2]} | Status: {item[3]}")
                no += 1

    elif pilihan == "3":
        print("\n[UBAH DATA]")
        if len(list_booking) == 0:
            print("Belum ada data untuk diubah.")
        else:
            for i in range(len(list_booking)):
                print(f"{i+1}. {list_booking[i][0]} - {list_booking[i][1]}")
            
            index = int(input("Pilih nomor data yang ingin diubah: ")) - 1
            if 0 <= index < len(list_booking):
                nama_lama = list_booking[index][0]
                lapangan_lama = list_booking[index][1]
                jam_lama = list_booking[index][2]
                status_pembayaran_lama = list_booking[index][3]

                lapangan_baru = input("Masukkan jenis lapangan baru (Futsal/Mini Soccer): ")
                jam_baru = input("Masukkan jam baru: ")
                status_pembayaran_baru = input("Masukkan status pembayaran baru: ")
                
                list_booking[index] = (nama_lama, lapangan_baru, jam_baru, status_pembayaran_baru)
                print("Data berhasil diubah.")
            else:
                print("Nomor data tidak ditemukan.")

    elif pilihan == "4":
        print("\n[HAPUS DATA]")
        if len(list_booking) == 0:
            print("Belum ada data untuk dihapus.")
        else:
            for i in range(len(list_booking)):
                print(f"{i+1}. {list_booking[i][0]} - {list_booking[i][1]}")
            
            index = int(input("Pilih nomor data yang ingin dihapus: ")) - 1
            if 0 <= index < len(list_booking):
                data_dihapus = list_booking.pop(index)
                print(f"Data atas nama {data_dihapus[0]} berhasil dihapus.")
            else:
                print("Nomor data tidak ditemukan.")

    elif pilihan == "5":
        print("Terima kasih, semoga hari Anda menyenangkan!")
        break

    else:
        print("Pilihan tidak valid, silakan coba lagi.")