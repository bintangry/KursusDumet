# Datatype adalah  jenis huruf dari nilai yang tersimpan didalam sebuah variable / kalimat yang  dicetak didalam print di python
# Jenis-jenis Datatype:

# 1. Integer -> Bilangan bulat tanpa desimal
# contoh: 1, 0, -10, 2025

usia = 10
tahun = 2025
nilaiUAS = 90

print(f' usia saya adalah {usia} tahun, sekarang tahun {tahun}, dan nilai UAS saya adalah {nilaiUAS}')

# 2. Float -> Bilangan desimal ( ada koma)
# contoh: 1.0, 0.0, -10.0, 2025.0

nilaiUTS = 8.5
beratbadan = 55.8
print(f'nilai UTS saya adalah {nilaiUTS}, dan berat badan saya adalah {beratbadan} kg')

# 3. String -> Teks yang dibungkus dengan tanda kutip

namalengkap = "Bintang Arya"
print(f' Nama lengkap saya adalah  {namalengkap}')

# 4. Boolean -> (True jika benar dan False jika salah)

statusMember = True 
print(f' {namalengkap} terdaftar sebagai member  di Dumetschool: {statusMember}')

# Tipe Data Kompleks:
# 1. List -> nilai yang tersimpan banyak lebih dari satu daidlam variable yang sifatnya mutable (dapat di manipulasi)
# 2. Tuple -> nilai yang tersimpan banyak lebih dari satu dalam variable yang sifatnya imutable (tidak dapat di manipulasi)
# 3. Disctionary -> nilai yg tersimpan banyak lebih dari satu didalam variable yang sifatnya imutable tapi untuk index batisnya
 #   pakai identitas string (assosiatif)

listsiswa = ['Bitang' , 'Brian' , 'Cindy']
listsiswa.append('Nanda')
print(f'berikut ini list data siswa Dumetschool: {listsiswa}')

# 2. Tuple
dataKaryawan = ('Iqbal' , 'Munir', 'Haikal')
print(f' Data Karyawan: {dataKaryawan[2]}')

# 3. Dictionary -> ('key' : 'value')
dataNasabah = {
    'namalengkap' : 'Bintang Arya',
    'usia': 19,
    'nilaiUAS': 90.5,
    'statusMember' : True,
    'alamat': 'Tangerang Selatan'
}

print(f'Data Nasabah Dumetschool {dataNasabah['namalengkap']}')
