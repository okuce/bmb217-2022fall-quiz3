from Cargo import Box

box1 = Box(0,0,0,"Bos")
box2 = Box(30,40,50,"Makarna")
box3 = Box(10,5,3,"Telefon")
box4 = Box(50,60,70,"TV")

total_price = 0
for box in [box1,box2,box3,box4]:
    total_price += box.price

print("Total:{}TL".format(total_price))


"""
Beklenen Ekran Çıktısı
Bos,0.0,0.0TL
Makarna,20.0,40TL
Telefon,0.05,20TL
TV,70.0,50TL
Total:110.0TL
"""