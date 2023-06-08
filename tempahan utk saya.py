jenis_bias = ["han","jungwon","haruto","soobin"]
harga_bias = [10000,20000,30000,40000]
jumlah = [0,1,2,3]

print("HARGA HAN= 10000, HARGA JUNGWON= 20000, HARGA HARUTO= 30000, HARGA SOOBIN=40000")
a=int(input("masukkan tempahan untuk HAN: "))
b=int(input("masukkan tempahan untuk JUNGWON: "))
c=int(input("masukkan tempahan untuk HARUTO: "))
d=int(input("masukkan tempahan untuk SOOBIN: "))

tempahan = [a,b,c,d]

def jumlah_harga() :
    for i in range(4) :
        jumlah[i] = harga_bias[i]*tempahan[i]
    return (jumlah)

def cetak() :
    print("\n\n Tempahan anda ialah: ")
    print(a,"bias", jenis_bias[0])
    print(b,"bias", jenis_bias[1])
    print(c,"bias", jenis_bias[2])
    print(d,"bias", jenis_bias[3])

    print("\n Jumlah harga untuk tempahan ialah RM",sum (jumlah))
jumlah_harga()
cetak()





    
    
    
    
    
    
    
    
    
    
    
    
    
    