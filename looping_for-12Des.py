# memiliki nilai sebanyak 5
buah = ['Apel', 'Mangga', 'Pisang', 'Jeruk', 'Semangka']

for x in buah:
# x adalah variabel yang akan menggantikan variabel 
# buah menjadi lebih sederhana

    if x == "Mangga":

        continue 
    # buah mangga akan diabaikan namun penyebutan terus berlanjut
    
    # if x == "Mangga":
        # untuk hentikan proses perulangan dan untuk data stroberi tidak akan dicetak
        # break

    # looping dengan data dalam bentuk data string
    # for y in "DUMETSCHOOL.COM":
    #     print(y)

    # mencetak variabel buah
    print(x)
    # yang muncul hanyalah apel, karena mangga itu batas akhir perulangan
    