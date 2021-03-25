#Rencana Pengujian

##Data Usia
usia_minimum = 21
usia = int(input("Berapa usia kamu?"))
usia_diterima = (usia >= usia_minimum)

##Data Kelulusan
ujian = input("Apakah Anda sudah lulus ujian kualifikasi (Y / T)?")
kelulusan_ujian = (ujian == "Y")

##Hasil Pengujian
if usia_diterima and kelulusan_ujian :
    print("Anda dapat mendaftar di kursus.")
else :
    print("Anda tidak dapat mendaftar di kursus.")


