import modules_company as mc
import platform
import sys
import math
import re
from math import factorial, sqrt

namaperusahaan = mc.company['name']
namaplatform = platform.system()

# menampilkan daftar simbol yang terdefinisi di modul platform
daftarsimbol = dir(platform)
direktori = sys.path
pi = math.pi
refile = re.__file__
faktor = factorial(6)
squareroot = math.sqrt(49)


print('')
print(namaperusahaan)
print('________________________________________')
print(namaplatform)
print('________________________________________')
print(daftarsimbol)
print('________________________________________')
print(direktori)
print('________________________________________')
print(pi)
print(round(pi, 2))
print("{:.2f}".format(pi))
print('________________________________________')
print(squareroot)
print(faktor)
print('________________________________________')
print(refile)
print('________________________________________')
for key, value in mc.company.items():
    print(key)
print('________________________________________')
for key, value in mc.company.items():
    print(value)
print('________________________________________')
for key, value in mc.company.items():
    print(f"{key}: {value}")
print('')
