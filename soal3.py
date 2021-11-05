teori = float(input("Nilai Ujian Teori : "))
praktek = float(input("Nilai Ujian Praktek : "))
if praktek>=70 and teori<70 :
    print("Anda harus mengulang ujian teori.")
elif praktek<70 and teori>=70 :
    print("Anda harus mengulang ujian praktek.") 
else :
    print("Selamat, Anda lulus!")