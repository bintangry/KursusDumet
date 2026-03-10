
# Membuat class dengan keyword class
# kelas tesebut diberi nama Matematika
class Matematika:
    

    #Deklarasi fungsi init
    def __init__(self, a, b):
        # deklarasi property dan value
        self.data1 = a
        self.data2 = b
    
    #membuat propert dengan nilai 1
    x = 1


# Membuat instance terhadap class matematika
obj = Matematika(8, 9)

# mencetak output dengan memanggil instance
# instance tersebut menjadi sebuah object
# selanjutnya object memanggil property yg ada didalam class
# istilah property disini biasa kita kenal dengan istilah variable
# fungsi in it???

print(obj.x)

print(f"{obj.data1} x {obj.data2} = {obj.data1} * {obj.data2} ")

