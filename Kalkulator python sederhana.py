from colorama import Fore
print(Fore.CYAN+'ini adalah program kalkulator sederhana python!\n'+Fore.RESET)

while True:
	pilihan_opsi=input('Pilih opsi(kali, bagi, tambah, kurang): ')

	if pilihan_opsi.lower()in['kali','perkalian','ร—']:
		angka_pertama_perkalian=input('Masukkan Angka pertama: ')
		angka_kedua_perkalian=input('Masukkan Angka ke dua:')
		hasil_perkalian=int(angka_pertama_perkalian)*int(angka_kedua_perkalian)
		print('Hasil: '+str(hasil_perkalian))
		break

	elif pilihan_opsi.lower()in['pembagian','bagi','รท']:
	    	angka_pertama_pembagian=input('Masukkan Angka pertama: ')
	    	angka_kedua_pembagian=input('Masukkan Angka ke dua: ')
	    	hasil_pembagian=int(angka_pertama_pembagian)/int(angka_kedua_pembagian)
	    	print('Hasil: '+str(hasil_pembagian))
	    	break

	elif pilihan_opsi.lower()in['tambah','pertambahan','+']:
	        angka_pertama_pertambahan=input('Masukkan Angka pertama: ')
	        angka_kedua_pertambahan=input('Masukkan Angka ke dua: ')
	        hasil_pertambahan=int(angka_pertama_pertambahan)+int(angka_kedua_pertambahan)
	        print('Hasil: '+str(hasil_pertambahan))
	        break

	elif pilihan_opsi.lower()in['kurang','pengurangan','-']:
	        angka_pertama_pengurangan=input('Masukkan Angka pertama: ')
	        angka_kedua_pengurangan=input('Masukkan Angka ke dua: ')
	        hasil_pengurangan=int(angka_pertama_pengurangan)-int(angka_kedua_pengurangan)
	        print('Hasil: '+str(hasil_pengurangan))
	        break

	else:
	    print(Fore.RED+'\nPilihan Tidak Valid Pilih opsi(kali, bagi, tambah, kurang)\n')
