class Book: 
    def __init__(self, title, price):
        self.judul = title
        self.__harga = price
        self.__diskon = None


    def set_discount(self, discount):
        self.__diskon = discount

    def get_discount(self):

        if self.__diskon:
            return self.__harga * (self.__diskon/100)
        return self.__harga
        
    def get_price(self):
        if self.__diskon: 
            return self.__harga - self.get_discount()
        return self.__harga
        
    def __repr__(self):
        return f'Book: {self.judul}, Price: {self.get_price()}'
    


buku = Book('start with why', 200000)
buku.set_discount(5)

print('Judul Buku: ', buku.judul)
print('Harga Buku sebelum Discount: ', buku.get_price() * buku.get_discount())
print('Diskon:', buku.get_discount())
print('Harga Buku setelah Discount: ', buku.get_price())




























#     def __init__(self, title):
#         self.judul = title
#         self.__diskon = 10


# buku = Book('Start With Why')


# print(buku.judul)
# print(buku.__diskon)

