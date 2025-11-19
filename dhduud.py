
#for i in range(1,11):
   # for j in range(1, i+1):
    #    print("%d " % (i*j), end='')
   # print()
   
   
   
   
list_nama = [
    {'nama' : 'falah', 'kelas' : 'B1', 'rata-rata nilai' : '90.1'},
    {'nama' : 'subansa', 'kelas' : 'B1', 'rata-rata nilai' : '88.6'},
    {'nama' : 'adiatma', 'kelas' : 'B1', 'rata-rata nilai' : '92.5'},
    {'nama' : 'rifai', 'kelas' : 'B1', 'rata-rata nilai' : '89.7'}
]



nama_siswa_dicari = input('Nama Siswa : ').lower()

for i, siswa in enumerate (list_nama):
    if siswa['nama'].lower() == nama_siswa_dicari:
        print(f"Nama : {siswa['nama']}")
        print(f"Kelas : {siswa['kelas']}")
        print(f"Rata-Rata Nilai : {siswa['rata-rata nilai']}")
        break
else:
    print("Nama siswa tidak ditemukan")
        
        
        




   
   