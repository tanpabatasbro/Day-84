print("""
    _____________________________
    |                           |
    |----------WELCOME----------|
    |---->>>>>WARNET KC<<<<<----|
    |___________________________|
    |                           |
    |  HARGA/JAM : RP. 3.000,00 |
    |  HARGA/MENIT : RP. 50,00  |
    |___________________________| 
    
    """)

nama = input("Nama Anda : ")
jamMasuk = int(input("Jam Masuk : "))
menitMasuk = int(input("Menit Masuk : "))
jamKeluar = int(input("Jam Keluar : "))
menitKeluar = int(input("Menit Keluar : "))

jamPakai = jamKeluar - jamMasuk
menitPakai = menitKeluar - menitMasuk

hasJamPakai = jamPakai * 3000
hasMenitPakai = menitPakai * 50
total = hasJamPakai + hasMenitPakai

print(f"\nNama       : {nama}")
print(f"Jam Pakai   : {jamPakai}")
print(f"Menit Pakai : {menitPakai}")
print(f"Harga Bayar : RP.{total},00")

print("\n---->>>>>THANK YOU<<<<<----\n")