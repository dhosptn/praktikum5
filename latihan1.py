# Buat dictionary daftar kontak
daftar_kontak = {
    'Ari': '081234567',
    'Dina': '085678912',
}

# Tampilkan kontak Ari
print(f"Nomor Ari: {daftar_kontak['Ari']}")

# Tambah kontak baru (Riko: 087654544)
daftar_kontak['Riko'] = '087654544'

# Ubah kontak Dina dengan nomor baru (088999776)
daftar_kontak['Dina'] = '088999776'

# Tampilkan semua Nama
print("Daftar Nama:")
for nama in daftar_kontak.keys():
    print(nama)

# Tampilkan semua Nomor
print("\nDaftar Nomor:")
for nomor in daftar_kontak.values():
    print(nomor)

# Tampilkan daftar Nama dan Nomornya
# header tabel
print("| {:<10} | {:<15} |".format("Nama", "Nomor"))

# garis pembatas
print("|{:=<12}|{:=<17}|".format("", ""))

# isi tabel
print("| {:<10} | {:<15} |".format("Ari", "081234567"))
print("| {:<10} | {:<15} |".format("Dina", "085678910"))
print("| {:<10} | {:<15} |".format("Riko", "087654544"))

# Hapus kontak Dina
del daftar_kontak['Dina']