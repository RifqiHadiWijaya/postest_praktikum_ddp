print('nama : Rifqi Hadi Wijaya')
print('nim : 2309116042')
print('kelas : sistem informsi-a')

#login sederhana
username = str(input('masukkan username : '))
password = str(input('masukkan password : '))

if password == "w12ry" :
    print('selamat datang rifqi')
else :
    print('password salah')
    exit(print('loginerror'))

#volume bangun ruang
print('bangun ruang')
bangun_ruang = str(input('pilih bangun ruang : '))

#bola
if bangun_ruang == 'bola' :
    jari2 = float(input('masukkan jari-jari : '))
    if jari2 % 7 == 0:
        phi = 22/7
    elif jari2 % 7 != 0:
        phi = 3.14
    bola = (4/3) * phi * jari2**3
    print(f"volume bola adalah : {bola}")
#tabung
elif bangun_ruang == 'tabung':
    jari2 = float(input('masukkan angka : '))
    if jari2 % 7 == 0:
        phi = 22/7
    elif jari2 % 7 != 0:
        phi = 3.14
    tinggi_tabung = float(input('masukkan tinggi tabung : '))
    tabung = phi * jari2**2 * tinggi_tabung
    print(f"volume tabung dalah : {tabung}")
#limas segitiga
elif bangun_ruang == 'limas segitiga' :
    luas_alas = float(input('masukkan alas limas : '))
    tinggi_limas = float(input('masukkan tinggi limas: '))
    volume_limas = 1/3 * luas_alas * tinggi_limas
    print(f"volume limas segitiga adalah : {volume_limas}")
else :
    print('bangun ruang tidak ada.')