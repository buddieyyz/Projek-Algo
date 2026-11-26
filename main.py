# =====================================================================
# SISTEM INVENTARIS DAN PEMINJAMAN TATA USAHA (TU) KAMPUS
# =====================================================================

# Simulasi Database Pengguna (Akun Login)
data_pengguna = {
    "admin": {"sandi": "admin123", "peran": "admin", "nama": "Petugas TU Kampus"},
    "henry": {"sandi": "mhs123", "peran": "mahasiswa", "nama": "Faisal Henry Bahresy"},
    "nezar": {"sandi": "mhs123", "peran": "mahasiswa", "nama": "Muhammad Nezar"},
}

# Simulasi Data Inventaris Barang
daftar_inventaris = [
    {"id_barang": "B001", "nama_barang": "Kabel HDMI 5m", "jumlah": 5, "kategori": "Elektronik"},
    {"id_barang": "B002", "nama_barang": "Proyektor Epson", "jumlah": 2, "kategori": "Elektronik"},
    {"id_barang": "B003", "nama_barang": "Kunci Ruang Seminar", "jumlah": 3, "kategori": "Kunci"},
    {"id_barang": "B004", "nama_barang": "Spidol Whiteboard Hitam", "jumlah": 15, "kategori": "ATK"}
]

# Simulasi Data Peminjaman
daftar_peminjaman = [
    {
        "id_peminjaman": "P001",
        "username": "henry",
        "nama_peminjam": "Faisal Henry Bahresy",
        "id_barang": "B001",
        "nama_barang": "Kabel HDMI 5m",
        "jumlah": 1,
        "status": "Dipinjam"
    }
]

# menampilkan header untuk setiap menu
def tampilkan_header(judul):
    print("=" * 60)
    print(f" {judul.center(56)} ")
    print("=" * 60)

def menu_login():
    tampilkan_header("SISTEM INVENTARIS & PEMINJAMAN TU KAMPUS")
    print("Silakan Login ke Sistem")
    print("-" * 30)
    username = input("Username : ").strip().lower()
    sandi = input("Password : ").strip()
    
    if username in data_pengguna and data_pengguna[username]["sandi"] == sandi:
        print(f"\n[OK] Login Berhasil! Selamat datang, {data_pengguna[username]['nama']}.")
        return username, data_pengguna[username]["peran"]
    else:
        print("\n[GAGAL] Username atau Password salah!")
        return None, None

# =====================================================================
# FITUR PENCARIAN BARANG (FITUR BARU)
# =====================================================================
def cari_barang():
    tampilkan_header("PENCARIAN BARANG INVENTARIS")
    keyword = input("Masukkan nama atau kategori barang yang dicari: ").strip().lower()
    
    hasil_pencarian = []
    for barang in daftar_inventaris:
        # Mencocokkan keyword dengan nama barang atau kategori (menggunakan in agar lebih fleksibel)
        if keyword in barang['nama_barang'].lower() or keyword in barang['kategori'].lower():
            hasil_pencarian.append(barang)
            
    if not hasil_pencarian:
        print(f"\n[INFO] Tidak ditemukan barang dengan kata kunci '{keyword}'.")
        return
        
    print(f"\n[SUKSES] Ditemukan {len(hasil_pencarian)} barang yang sesuai:")
    print(f"{'ID':<6} | {'Nama Barang':<25} | {'Jumlah':<8} | {'Kategori':<15}")
    print("-" * 62)
    for barang in hasil_pencarian:
        print(f"{barang['id_barang']:<6} | {barang['nama_barang']:<25} | {barang['jumlah']:<8} | {barang['kategori']:<15}")

# =====================================================================
# FITUR ADMIN / TATA USAHA
# =====================================================================
def menu_admin(username):
    while True:
        tampilkan_header("PANEL ADMIN / TATA USAHA")
        print("1. Lihat Daftar Inventaris")
        print("2. Tambah Barang Baru")
        print("3. Ubah / Restock Jumlah Barang")
        print("4. Hapus Barang")
        print("5. Lihat Semua Permohonan & Peminjaman Mahasiswa")
        print("6. Konfirmasi Status Peminjaman (Setujui / Selesai)")
        print("7. Cari Barang")
        print("8. Logout")
        pilihan = input("\nPilih menu (1-8): ").strip()
        
        if pilihan == "1":
            tampilkan_inventaris()
        elif pilihan == "2":
            tambah_barang()
        elif pilihan == "3":
            ubah_stok_barang()
        elif pilihan == "4":
            hapus_barang()
        elif pilihan == "5":
            lihat_semua_peminjaman()
        elif pilihan == "6":
            konfirmasi_peminjaman()
        elif pilihan == "7":

            cari_barang()
        elif pilihan == "8":

            print("\nLogout berhasil. Keluar dari Panel Admin...")
            break
        else:
            print("\nPilihan tidak valid. Silakan coba lagi.")
        input("\nTekan Enter untuk melanjutkan...")

def tampilkan_inventaris():
    tampilkan_header("KATALOG INVENTARIS TU")
    if not daftar_inventaris:
        print("Belum ada data inventaris.")
        return
    
    print(f"{'ID':<6} | {'Nama Barang':<25} | {'Jumlah':<8} | {'Kategori':<15}")
    print("-" * 62)
    for barang in daftar_inventaris:
        print(f"{barang['id_barang']:<6} | {barang['nama_barang']:<25} | {barang['jumlah']:<8} | {barang['kategori']:<15}")

def tambah_barang():
    tampilkan_header("TAMBAH BARANG BARU")
    id_barang = input("Masukkan ID Barang (contoh: B005): ").strip().upper()
    
    for barang in daftar_inventaris:
        if barang['id_barang'] == id_barang:
            print("[GAGAL] ID Barang sudah terdaftar di sistem!")
            return
            
    nama_barang = input("Masukkan Nama Barang: ").strip()
    try:
        jumlah = int(input("Masukkan Jumlah Stok: ").strip())
        if jumlah < 0:
            print("[GAGAL] Jumlah tidak boleh negatif.")
            return
    except ValueError:
        print("[GAGAL] Input jumlah harus berupa angka!")
        return
        
    kategori = input("Masukkan Kategori (misal: Elektronik, ATK, Kunci): ").strip()
    
    daftar_inventaris.append({
        "id_barang": id_barang,
        "nama_barang": nama_barang,
        "jumlah": jumlah,
        "kategori": kategori
    })
    print(f"\n[SUKSES] Barang '{nama_barang}' berhasil ditambahkan ke inventaris!")

def ubah_stok_barang():
    tampilkan_header("UBAH / RESTOCK JUMLAH BARANG")
    tampilkan_inventaris()
    id_barang = input("\nMasukkan ID Barang yang ingin diubah: ").strip().upper()
    
    target_barang = None
    for barang in daftar_inventaris:
        if barang['id_barang'] == id_barang:
            target_barang = barang
            break
            
    if not target_barang:
        print("[GAGAL] Barang dengan ID tersebut tidak ditemukan.")
        return
        
    print(f"Barang dipilih: {target_barang['nama_barang']} (Stok saat ini: {target_barang['jumlah']})")
    try:
        jumlah_baru = int(input("Masukkan jumlah stok yang baru: ").strip())
        if jumlah_baru < 0:
            print("[GAGAL] Jumlah tidak boleh negatif.")
            return
        target_barang['jumlah'] = jumlah_baru
        print(f"\n[SUKSES] Stok barang '{target_barang['nama_barang']}' berhasil diperbarui menjadi {jumlah_baru}.")
    except ValueError:
        print("[GAGAL] Input jumlah harus berupa angka!")

def hapus_barang():
    tampilkan_header("HAPUS BARANG DARI INVENTARIS")
    tampilkan_inventaris()
    id_barang = input("\nMasukkan ID Barang yang ingin dihapus: ").strip().upper()
    
    index_target = -1
    for i, barang in enumerate(daftar_inventaris):
        if barang['id_barang'] == id_barang:
            index_target = i
            break
            
    if index_target == -1:
        print("[GAGAL] Barang dengan ID tersebut tidak ditemukan.")
        return
        
    barang_dihapus = daftar_inventaris.pop(index_target)
    print(f"\n[SUKSES] Barang '{barang_dihapus['nama_barang']}' berhasil dihapus dari sistem.")

def lihat_semua_peminjaman():
    tampilkan_header("DAFTAR PERMOHONAN & RIWAYAT PEMINJAMAN")
    if not daftar_peminjaman:
        print("Belum ada data peminjaman.")
        return
        
    print(f"{'ID Pinjam':<10} | {'Peminjam':<15} | {'Barang':<20} | {'Jumlah':<6} | {'Status':<22}")
    print("-" * 83)
    for pinjam in daftar_peminjaman:
        print(f"{pinjam['id_peminjaman']:<10} | {pinjam['nama_peminjam']:<15} | {pinjam['nama_barang']:<20} | {pinjam['jumlah']:<6} | {pinjam['status']:<22}")

def konfirmasi_peminjaman():
    tampilkan_header("KONFIRMASI STATUS PEMINJAMAN")
    if not daftar_peminjaman:
        print("Belum ada data peminjaman.")
        return
        
    lihat_semua_peminjaman()
    id_pinjam = input("\nMasukkan ID Peminjaman yang ingin dikonfirmasi: ").strip().upper()
    
    target_pinjam = None
    for pinjam in daftar_peminjaman:
        if pinjam['id_peminjaman'] == id_pinjam:
            target_pinjam = pinjam
            break
            
    if not target_pinjam:
        print("[GAGAL] ID Peminjaman tidak ditemukan.")
        return
        
    print(f"\nStatus saat ini: {target_pinjam['status']}")
    print("Pilih Update Status:")
    print("1. Setujui (Sedang Dipinjam)")
    print("2. Selesai (Barang Telah Dikembalikan)")
    print("3. Tolak / Batalkan Peminjaman")
    
    pilihan_status = input("Pilihan (1-3): ").strip()
    
    if pilihan_status == "1":
        target_pinjam['status'] = "Dipinjam"
        print("[SUKSES] Status diperbarui menjadi: Dipinjam.")
    elif pilihan_status == "2":
        if target_pinjam['status'] != "Dikembalikan":
            for barang in daftar_inventaris:
                if barang['id_barang'] == target_pinjam['id_barang']:
                    barang['jumlah'] += target_pinjam['jumlah']
                    break
            target_pinjam['status'] = "Dikembalikan"
            print("[SUKSES] Status diperbarui menjadi: Dikembalikan (Stok barang dikembalikan ke TU).")
        else:
            print("Barang ini sudah berstatus dikembalikan sebelumnya.")
    elif pilihan_status == "3":
        if target_pinjam['status'] == "Menunggu Persetujuan":
            for barang in daftar_inventaris:
                if barang['id_barang'] == target_pinjam['id_barang']:
                    barang['jumlah'] += target_pinjam['jumlah']
                    break
        target_pinjam['status'] = "Ditolak / Batal"
        print("[INFO] Peminjaman ditolak atau dibatalkan.")
    else:
        print("[GAGAL] Pilihan tidak valid.")

# =====================================================================
# FITUR PEMINJAM (MAHASISWA)
# =====================================================================
def menu_mahasiswa(username):
    nama_mhs = data_pengguna[username]["nama"]
    while True:
        tampilkan_header(f"PANEL MAHASISWA ({nama_mhs})")
        print("1. Lihat Katalog Barang & Ketersediaan")
        print("2. Ajukan Permohonan Peminjaman Barang")
        print("3. Lihat Status & Riwayat Peminjaman Saya")
        print("4. Cari Barang")
        print("5. Logout")
        pilihan = input("\nPilih menu (1-5): ").strip()
        
        if pilihan == "1":
            tampilkan_inventaris()
        elif pilihan == "2":
            ajukan_peminjaman(username, nama_mhs)
        elif pilihan == "3":
            lihat_riwayat_mahasiswa(username)
        elif pilihan == "4":
            cari_barang()
        elif pilihan == "5":
            print("\nLogout berhasil. Keluar dari Panel Mahasiswa...")
            break
        else:
            print("\nPilihan tidak valid. Silakan coba lagi.")
        input("\nTekan Enter untuk melanjutkan...")

def ajukan_peminjaman(username, nama_mhs):
    tampilkan_header("AJUKAN PEMINJAMAN BARANG")
    tampilkan_inventaris()
    
    id_barang = input("\nMasukkan ID Barang yang ingin dipinjam: ").strip().upper()
    target_barang = None
    for barang in daftar_inventaris:
        if barang['id_barang'] == id_barang:
            target_barang = barang
            break
            
    if not target_barang:
        print("[GAGAL] Barang dengan ID tersebut tidak ditemukan.")
        return
        
    print(f"Barang dipilih: {target_barang['nama_barang']} (Stok tersedia: {target_barang['jumlah']})")
    if target_barang['jumlah'] <= 0:
        print("[GAGAL] Maaf, stok barang ini sedang habis.")
        return
        
    try:
        jumlah_pinjam = int(input("Masukkan jumlah yang ingin dipinjam: ").strip())
        if jumlah_pinjam <= 0:
            print("[GAGAL] Jumlah peminjaman harus lebih dari 0.")
            return
        if jumlah_pinjam > target_barang['jumlah']:
            print("[GAGAL] Jumlah peminjaman melebihi stok yang tersedia!")
            return
    except ValueError:
        print("[GAGAL] Input jumlah harus berupa angka!")
        return
        
    target_barang['jumlah'] -= jumlah_pinjam
    id_peminjaman = f"P0{len(daftar_peminjaman) + 1:02d}"
    
    daftar_peminjaman.append({
        "id_peminjaman": id_peminjaman,
        "username": username,
        "nama_peminjam": nama_mhs,
        "id_barang": id_barang,
        "nama_barang": target_barang['nama_barang'],
        "jumlah": jumlah_pinjam,
        "status": "Menunggu Persetujuan"
    })
    print(f"\n[SUKSES] Permohonan berhasil diajukan dengan ID {id_peminjaman}! Menunggu konfirmasi Admin TU.")

def lihat_riwayat_mahasiswa(username):
    tampilkan_header("RIWAYAT PEMINJAMAN SAYA")
    
    riwayat_ada = False
    print(f"{'ID Pinjam':<10} | {'Nama Barang':<20} | {'Jumlah':<6} | {'Status':<22}")
    print("-" * 64)
    for pinjam in daftar_peminjaman:
        if pinjam['username'] == username:
            riwayat_ada = True
            print(f"{pinjam['id_peminjaman']:<10} | {pinjam['nama_barang']:<20} | {pinjam['jumlah']:<6} | {pinjam['status']:<22}")
            
    if not riwayat_ada:
        print("Anda belum pernah mengajukan peminjaman barang.")

# =====================================================================
# PROGRAM UTAMA (MAIN ROUTINE)
# =====================================================================
def utama():
    while True:
        username, peran = menu_login()
        if username and peran:
            if peran == "admin":
                menu_admin(username)
            elif peran == "mahasiswa":
                menu_mahasiswa(username)
        else:
            ulang = input("\nIngin coba login lagi? (y/n): ").strip().lower()
            if ulang == 'n':
                print("\nTerima kasih telah menggunakan Sistem Inventaris TU Kampus!")
                break

if __name__ == "__main__":
    utama()