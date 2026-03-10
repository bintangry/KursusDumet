print('')
print('')
print('==========================================')
print("##Belajar for nested bagian pertama##")
print('==========================================')

for g in range(10):
    for f in range(g+1):
        print(f, end='') #fungsi end supaya tidak kebawah
    print()

print('')
print('')
print('==========================================')
print("##Belajar for nested bagian kedua##")
print('==========================================')

for g in range(10):
    for f in range(g+1):
        print('*', end='') # fungsi end supaya tidak kebawah
    print()



print('')
print('')
print('==========================================')
print("##Belajar for nested bagian ketiga##")
print('==========================================')

r = 10

s = r - 1

for t in range(0, r):
    for j in range (0, s):

        print ( ' ',  end = '') #fungsi end supaya tidak kebawah

    s -= 1
    for j in range(0 , t + 1):
        print('* ', end = '') #fungsi end supaya tidak kebawah
    print('')
                


print('')
print('')

