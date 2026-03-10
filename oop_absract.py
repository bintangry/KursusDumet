class Kendaraan:
    # Jika sebuah method pada oop tidak diberikan argumen atau
    # parameter self maka akan terjadi error / tidak dapat dipanggil
    def merk(self):
        print('Mobil saya adalah Toyota')

class Mobil(Kendaraan):
    # Jika sebuah method tidak diberikan argumen / parameter self maka akan
    # terjadi error dan tidak dapat dipanggil
    # def merk(self):
    #     print('Merk Mobil Saya adalah Mazda')
    pass


object = Mobil()

# akan error ketika memanggil method merk()
# karena tidak mendefinisikan argumen self
object.merk()
