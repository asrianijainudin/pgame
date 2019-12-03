d="Ini Merupakan Perulangan While"	# perulangan “while”
print(d)
x = 0
while (x < 5): 	# jika x lebih kecil dari 5 maka ulangi
# 	x = x + 1
	x += 1 			# x + 1
	print(" Asriani ")

j="Ini Merupakan Perulangan For"	# perulangan “for”
print(j)
for x in range(5):
	print("Asriani")

a="Ini Merupakan Fungsi / Function"	# Fungsi / Function
print(a)
# Fungsi / Function
def tambah_1(d,j):
	a = d + j
	print(a) # langsung cetak hasil

def tambah_2(d,j):
	a = d + j
	return a # mengembalikan nilai, disimpan dalam fungsi

# cara memanggil kedua fungsi tersebut
tambah_1(17,7)
print(tambah_2(57,7))

# memanggil fungsi dengan variable
d=34
j=36
tambah_1(d,j)
print(tambah_2(d,j))
