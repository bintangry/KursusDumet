# OOP (Object Orianted Programming) adalah pemrograman berorientasi kepada sebuah objek.
# yaitu konsep pemorgraman yang mengorganisir kode berdasarkan objek 
# sedangkan pemrograman biasa berbasis prosedural hanya ber-fokus pada fungsi.
# dan OOP fokus kepada objek = perilaku (method yang ada didalam class)


# Konsep OOP ada 4 pilar:
# 1. Class -> blueprint yg membungkus method-method didalamnya
# 2. Method -> kumpulan blok yang dibuat menggunakan fungsi didalam class
# 3. Objek -> Inheritance / Perubahan dari class
# 4. Inheritance -> Pewarisan sifat dari class lain


# Membuat class siswa (blueprint)
class Siswa:

    # Ini adalah method construct (yaitu sebuah metode method default bawaan oop python yang didjalankan pertama kali)
    def __init__(self, nama, nilai):
        self.nama = nama # membuat atribut nama dan nilainya diambil dari statement yang ada didalam kurung (self, nama, nilai)
        self.nilai = nilai 

    def rataRata(self): # method untuk menghitung rata-rata
        return sum(self.nilai) / len(self.nilai)
    
    def status(self):
        if self.rataRata() >= 75:
            return "LULUS"
        else:
            return "TIDAK LULUS"
        
    def info(self):
        print("nama:        ", self.nama)
        print("Nilai        "self.nilai)
        print("Rata-rata     :"self.rataRata())
        print("Status        :" self.status())

        # Membuat object dari class siswa
        siswa1 = Siswa("Bintang Arya", [90, 85, 95])
        siswa2 = Siswa("Brian", [95, 70, 65])

        #disini penutup class/akhir dari class

        # Membuat Objek dari class siswa 
        siswa1



    