print('')
print('==========================')
print(' Merubah item pada array')
print('===========================')

import array as arr
numbers = arr.array('i', [10, 20, 30, 40, 50])

print('Nilai sebelum diubah adalah', numbers)

# ubah elements terakhir
numbers[2] = 40

print ('Nilai setelah diubah adalah', numbers)

print('')