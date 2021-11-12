
nama = []
nohp = []
def menu() :
    print ('Selamat datang !\n')
    print ('--Menu--')
    print ('1. Daftar Kontak')
    print ('2. Tambah Kontak')
    print ('3. Keluar')

def daftar_kontak() :
    if len(nama and nohp) <= 0:
        print ('belum ada kontak')
    else :
        for indeks in range(len(nama and nohp)):
            print('Nama: {}'.format(nama[indeks]))
            print('No Telepon: {}'.format(nohp[indeks]))
          

def tambah_kontak() :
    nama_baru = input('Nama: ')
    nama.append(nama_baru)
    nohp_baru = input('No Telepon: ')
    nohp.append(nohp_baru)

def pesan() :
    print ('Kontak berhasil ditambahkan')

#program utama
while True :
    menu()
    pilih =input("Pilih Menu : ")
    if pilih == ('1') : daftar_kontak()
    elif pilih == ('2') : tambah_kontak() , pesan()
    elif pilih == ('3') : print('Program selesai, sampai jumpa!')
    else : print('Menu tidak tersedia')

        
         