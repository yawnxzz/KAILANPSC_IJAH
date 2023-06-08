jenis_kek = ["keju","mentega","pelangi","kopi"]
harga_kek = [40,35,25,15]
jumlah = [0,1,2,3]

print("HARGA KEK KEJU=RM40, MENTEGA=RM35, PELANGI=25, KOPI=15")
a=int(input("masukkan tempahan untuk kek keju:"))
b=int(input("masukkan tempahan untuk kek mentega:"))
c=int(input("masukkan tempahan untuk kek pelangi:"))
d=int(input("masukkan tempahan untuk kek kopi:"))

tempahan = [a,b,c,d]

def jumlah_harga() :
    for i in range(4) :
        jumlah[i] = harga_kek[i]*tempahan[i]
    return(jumlah)

def cetak() : 
    print("\n\n Tempahan anda ialah:")   
    print(a,"kek", jenis_kek[0])  
    print(b,"kek", jenis_kek[1])
    print(c,"kek", jenis_kek[2])
    print(d,"kek", jenis_kek[3])

    print("\n Jumlah harga untuk tempahan ialah RM",sum (jumlah))
jumlah_harga()    
cetak()