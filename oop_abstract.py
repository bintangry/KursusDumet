from abc import ABC, abstractmethod

# Membuat class kendaraan menjadi abstract
# dengan memberikan argumen dengan nilai ABC
# maka class kendaraan menjadi bastract
class Kendaraan(ABC):
    # Membuat method merk menjadi abstract
    # diawali dengan tanda @
    @abstractmethod
    def merk(self):
        pass
        #print('Merk Mobil Saya adalah Toyota')


class Mobil(Kendaraan):
    def merk(self):
        print('Merk mobil saya adalah mazda')

object = Mobil()


# tes apakah bisa diakses
# tidak bisa diakses karena sifatnya abstract
object.merk()