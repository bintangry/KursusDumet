# Membuat properti dengan nama y berada didalam ruang lingkup global
y = 5
# Membuat sebuah fungsi / method ndengan nama angka
def angka():
    print('Dari dalam fungsi:', y)

angka()

# Mengakses properti y dari luar fungsi
print('dari luar fungsi', y)