# program membuat persegi dengan simbol bintang, dengan input dari user
# contoh persegi
#     *****
#     *****
#     *****
#     *****
#     *****
# misal
sisi = int(input("Masukkan panjang sisi : "))
# membuat persegi dengan simbol bintang
for asep in range(sisi):
    bintang =""
    for udin in range(sisi):
        bintang += "*"
    print(bintang)