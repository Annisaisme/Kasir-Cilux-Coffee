
print('\n\t\t~\tCILUX Coffee\t~')
print('\n\tBerikut adalah manu yang kami sediakan')
print('\t(Cukup tuliskan digit angka pada menu)')
print('\t  (tulis "stop" jika selesai memesan)')

print('\n\t\t- COFFEE -')
print('\t1. Americano\t\tRp 28.000\n\t2. Cafe Latte\t\tRp 30.000\n\t3. Mocha Latte\t\tRp 35.000\n\t4. Cappuccino\t\tRp 30.000\n\t5. Caramel Latte\tRp 36.000\n\t6. Hazelnut Latte\tRp 35.000\n\t7. Matcha Latte\t\tRp 30.000\n\t8. Vanilla Latte\tRp 33.000\n\t9. Black Coffee\t\tRp  8.000\n\t10. Robusta Coffee\tRp 10.000\n\t11. Arabica Coffee\tRp 15.000')

print('\n\t\t- NONCOFFEE -')
print('\t12. Tea\t\t\tRp  5.000\n\t13. Lemon Tea\t\tRp  8.000\n\t14. Thai tea\t\tRp 10.000')

print('\n\t\t- FRAPPE -')
print('\t15. Chocolate\t\tRp 20.000\n\t16. Vanilla\t\tRp 20.000\n\t17. Red Velvet\t\tRp 20.000\n\t18. Taro\t\tRp 20.000\n\t19. Strawberry\t\tRp 20.000\n\t20. Green Tea\t\tRp 20.000')

print('\n\t\t- SNACK -')
print('\n\t21. French Fries\tRp 10.000\n\t22. Burger\t\tRp 15.000\n\t23. Pancake\t\tRp 15.000\n\t24. Egg Stick\t\tRp  7.000\n\t25. Nuggets\t\tRp 15.000\n\t26. Bread\t\tRp 10.000\n\t27. Pudding\t\tRp 10.000\n\t28. Ice Cream\t\tRp 15.000')

print('\n\t\t- FOOD -')
print('\n\t29. Nasi Goreng\t\tRp 12.000\n\t30. Mie Kuah\t\tRp 10.000\n\t31. Mie Goreng\t\tRp 10.000')

Hitung = 0
Bayar = 0
Total = []
ListMenu = []
MenuNya = ["Americano","Cafe Latte","Mocha Latte","Cappuccino","Caramel Latte","Hazelnut Latte","Matcha Latte","Vanilla Latte","Black Coffee","Robusta Coffee","Arabica Coffee","Tea","Lemon Tea","Thai Tea","Chocolate","Vanilla","Red Velvet","Taro","Strawberry","Green Tea","French Fries","Burger","Pancake","Egg Stick","Nuggets","Bread","Pudding","Ice Cream","Nasi Goreng","Mie Kuah","Mie Goreng"]

Americano = ['1']
Cafe_latte = ['2']
mocha_latte = ['3']
Cappuccino = ['4']
Caramel_latte = ['5']
Hazelnut_latte = ['6']
Matcha_latte= ['7']
Vanilla_latte= ['8']
Black_coffee= ['9']
Robusta_coffee= ['10']
Arabica_coffee= ['11']
Tea = ['12']
Lemon_tea= ['13']
Thai_tea= ['14']
Chocolate= ['15']
Vanilla= ['16']
Red_velvet= ['17']
Taro= ['18']
Strawberry= ['19']
Green_tea= ['20']
French_fries= ['21']
Burger= ['22']
Pancake= ['23']
Egg_stick= ['24']
Nuggets= ['25']
Bread= ['26']
Pudding= ['27']
Ice_cream= ['28']
Nasi_goreng= ['29']
Mie_kuah= ['30']
Mie_goreng= ['31']
sTop = ['Stop','stop','STOP','Sudah','sudah','Cukup','cukup','selesai','Selesai']

meja = input('\nBerapa nomor meja anda : ')

while True:
    menu = input('\nMasukkan digit angka pesanan anda : ')
    if menu in Americano:
            Harga = 28000
            Total.append(Harga)
            ListMenu.append(MenuNya[0])
            print(MenuNya[0],"Harga Rp ",Harga)
    elif menu in Cafe_latte:
            Harga = 30000
            Total.append(Harga)
            ListMenu.append(MenuNya[1])
            print(MenuNya[1],"Harga Rp ",Harga)
    elif menu in mocha_latte:
            Harga = 35000
            Total.append(Harga)
            ListMenu.append(MenuNya[2])
            print(MenuNya[2],"Harga Rp ",Harga)
    elif menu in Cappuccino:
            Harga = 30000
            Total.append(Harga)
            ListMenu.append(MenuNya[3])
            print(MenuNya[3],"Harga Rp ",Harga)
    elif menu in Caramel_latte:
            Harga = 36000
            Total.append(Harga)
            ListMenu.append(MenuNya[4])
            print(MenuNya[4],"Harga Rp ",Harga)
    elif menu in Hazelnut_latte:
            Harga = 35000
            Total.append(Harga)
            ListMenu.append(MenuNya[5])
            print(MenuNya[5],"Harga Rp ",Harga)
    elif menu in Matcha_latte:
            Harga = 30000
            Total.append(Harga)
            ListMenu.append(MenuNya[6])
            print(MenuNya[6],"Harga Rp ",Harga)
    elif menu in Vanilla_latte:
            Harga = 33000
            Total.append(Harga)
            ListMenu.append(MenuNya[7])
            print(MenuNya[7],"Harga Rp ",Harga)
    elif menu in Black_coffee:
            Harga = 8000
            Total.append(Harga)
            ListMenu.append(MenuNya[8])
            print(MenuNya[8],"Harga Rp ",Harga)
    elif menu in Robusta_coffee:
            Harga = 10000
            Total.append(Harga)
            ListMenu.append(MenuNya[9])
            print(MenuNya[9],"Harga Rp ",Harga)
    elif menu in Arabica_coffee:
            Harga = 15000
            Total.append(Harga)
            ListMenu.append(MenuNya[10])
            print(MenuNya[10],"Harga Rp ",Harga)
    elif menu in Tea:
            Harga = 5000
            Total.append(Harga)
            ListMenu.append(MenuNya[11])
            print(MenuNya[11],"Harga Rp ",Harga)
    elif menu in Lemon_tea:
            Harga = 8000
            Total.append(Harga)
            ListMenu.append(MenuNya[12])
            print(MenuNya[12],"Harga Rp ",Harga)
    elif menu in Thai_tea:
            Harga = 10000
            Total.append(Harga)
            ListMenu.append(MenuNya[13])
            print(MenuNya[13],"Harga Rp ",Harga)
    elif menu in Chocolate:
            Harga = 20000
            Total.append(Harga)
            ListMenu.append(MenuNya[14])
            print(MenuNya[14],"Harga Rp ",Harga)
    elif menu in Vanilla:
            Harga = 20000
            Total.append(Harga)
            ListMenu.append(MenuNya[15])
            print(MenuNya[15],"Harga Rp ",Harga)
    elif menu in Red_velvet:
            Harga = 20000
            Total.append(Harga)
            ListMenu.append(MenuNya[16])
            print(MenuNya[16],"Harga Rp ",Harga)
    elif menu in Taro:
            Harga = 20000
            Total.append(Harga)
            ListMenu.append(MenuNya[17])
            print(MenuNya[17],"Harga Rp ",Harga)
    elif menu in Strawberry:
            Harga = 20000
            Total.append(Harga)
            ListMenu.append(MenuNya[18])
            print(MenuNya[18],"Harga Rp ",Harga)
    elif menu in Green_tea:
            Harga = 20000
            Total.append(Harga)
            ListMenu.append(MenuNya[19])
            print(MenuNya[19],"Harga Rp ",Harga)
    elif menu in French_fries:
            Harga = 10000
            Total.append(Harga)
            ListMenu.append(MenuNya[20])
            print(MenuNya[20],"Harga Rp ",Harga)
    elif menu in Burger:
            Harga = 15000
            Total.append(Harga)
            ListMenu.append(MenuNya[21])
            print(MenuNya[21],"Harga Rp ",Harga)
    elif menu in Pancake:
            Harga = 15000
            Total.append(Harga)
            ListMenu.append(MenuNya[22])
            print(MenuNya[22],"Harga Rp ",Harga)
    elif menu in Egg_stick:
            Harga = 7000
            Total.append(Harga)
            ListMenu.append(MenuNya[23])
            print(MenuNya[23],"Harga Rp ",Harga)
    elif menu in Nuggets:
            Harga = 15000
            Total.append(Harga)
            ListMenu.append(MenuNya[24])
            print(MenuNya[24],"Harga Rp ",Harga)
    elif menu in Bread:
            Harga = 10000
            Total.append(Harga)
            ListMenu.append(MenuNya[25])
            print(MenuNya[25],"Harga Rp ",Harga)
    elif menu in Pudding:
            Harga = 10000
            Total.append(Harga)
            ListMenu.append(MenuNya[26])
            print(MenuNya[26],"Harga Rp ",Harga)
    elif menu in Ice_cream:
            Harga = 15000
            Total.append(Harga)
            ListMenu.append(MenuNya[27])
            print(MenuNya[27],"Harga Rp ",Harga)
    elif menu in Nasi_goreng:
            Harga = 12000
            Total.append(Harga)
            ListMenu.append(MenuNya[28])
            print(MenuNya[28],"Harga Rp ",Harga)
    elif menu in Mie_kuah:
            Harga = 10000
            Total.append(Harga)
            ListMenu.append(MenuNya[29])
            print(MenuNya[29],"Harga Rp ",Harga)
    elif menu in Mie_goreng:
            Harga = 10000
            Total.append(Harga)
            ListMenu.append(MenuNya[30])
            print(MenuNya[30],"Harga Rp ",Harga)
    elif menu in sTop:
            print('\nNomor meja : ', meja)
            print('Berikut pesanan anda : ')
            for list in ListMenu:
                    print("Makanan ke-{} = ". format(Hitung+1),list,'\tHarga Rp ', Total[Hitung])
                    Hitung +=1
            print('\nTotal tagihan anda sejumlah Rp ', sum(Total))
            print('Silahkan melakukan pembayaran dikasir')
            break
    else:
        print('Mohon maaf, nomor pesanan yang anda masukkan tidak tersedia di daftar menu')
        menu