Capstone Project Module 1 - Faza Syafri Nur Rahman - JCDS-1904-015

Membuat Aplikasi Data Pasien Rumah Sakit 

•	Pemrograman project ini menggunakan python.
•	Data collection, Conditional statement, Looping, penggunaan def function dan beberapa fungsi tambahan lain.
•	Masing-masing study case minimal memiliki 5 Field (Kolom / Keys) dengan 1 Unique Kolom.

ISI PROGRAM:
Terdapat Read, Create, Update, dan Delete di dalam program ini.
Sebelum terdapat dictionary yang berisi data pasien berupa :
a.	ID_Pasien = merupakan unique id (key) dari setiap pasien
b.	Nama Pasien
c.	Umur Pasien
d.	Golongan darah = nantinya golongan darah ini hanya bisa menerima input A, B, O, AB
e.	Alamat 
f.	Status Pasien


Isi dari aplikasi:
1.	Read ( Membaca List Pasien )
    a.	Memanggil Semua Data Pasien Yang Ada Di Dalam Dictionary
        Dimenu ini user akan langsung ditampilkan semua data yang ada didalam data pasien (ListPasien)

    b.	Memanggil Data Pasien Berdasarkan Kode Pasien (ID Pasien)
        Di menu ini user dapat menampilkan data pasien hanya dengan menginput kode pasiennya saja, jika ada data akan tampil namun jika tidak ada maka akan muncul             notif bahwa data pasien yang dicari tidak ada.

    c.	Memanggil Data Pasien Berdasarkan Nama Pasien
    d.	Di menu ini user dapat menampilkan data pasien hanya dengan menginput nama pasiennya saja, jika ada data akan tampil namun jika tidak ada maka akan muncul             notif bahwa data pasien yang dicari tidak ada.

    e.	Memanggil Data Pasien Berdasarkan Status Pasien
        Di menu ini user dapat menampilkan data pasien hanya dengan menginput status pasiennya saja, jika ada data akan tampil namun jika tidak ada maka akan muncul           notif bahwa data pasien yang dicari tidak ada.

    f.	Kembali Ke Menu Utama / Menu sebelumnya.
        Kembali ke menu utama dimana di dalamnya terdapat konfirmasi yes (y) or no (n), penggunaan while loop dan if else statement sebagai fungsi anti-typo, jika typo         atau pilihan tidak ada dia akan kemabli ke konfirmasi.


    Semua pilihan di atas (kecuali exit menu) akan menampilkan dictionary berupa:

    a.	ID_Pasien = merupakan unique id dari setiap pasien
    b.	Nama Pasien
    c.	Umur Pasien = umur hanya dapat berisi angka saja
    d.	Golongan darah = nantinya golongan darah ini hanya bisa menerima input A, B, O, AB
    e.	Alamat KTP
    f.	Status Pasien = hanya berisi rawat inap atau rawat jalan 

2.	Create ( Menambahkan Pasien )
    Di dalam menu tambah pasien terdapat 2 menu:

    a.	Tambah Pasien
        Di menu ini user dapat menambahkan pasien baru ke dalam data pasien (ListPasien) dimana didalamnya inputan nomor pasien baru akan di cek terlebih dahulu, jika         tidak tersedia maka aka nada notif bahwa kode sudah digunakan , jika tersedia maka akan lanjut ke pengisian kelengkapan data oleh user yang dimana akan ada             opsi konfirmasi apakah akan disimpan atau tidak. Jika disimpan maka data tadi akan tersimpan di data pasien (ListPasien), jika tidak maka akan Kembali ke menu         tambah pasien.

    b.	Kembali ke Menu Utama
        Kembali ke menu utama dimana di dalamnya terdapat konfirmasi yes (y) or no (n), penggunaan while loop dan if else statement sebagai fungsi anti-typo, jika typo         atau pilihan tidak ada dia akan kemabli ke konfirmasi.

3.	Update ( Memperbaharui Data Pasien )
    Di dalam menu ini terdapat 3 sub menu:
    a.	Ubah data pasien secara menyeluruh
        Di menu ini user dapat mengubah data 1 unique code ( pasien) secara menyeluruh dari nama hingga status, dengan konfirmasi pertama yaitu melanjutkan peruabahan         atau tidak dan konfirmasi kedua menyimpan perubahan atau tidak. Disini proses pengimputan data sama seperti ketika menginput data untuk pasien baru

    b.	Ubah data pasien per kolom
        Di menu ini user dapat mengubah data 1 unique code ( pasien) secara menyeluruh dari nama hingga status, dengan konfirmasi pertama yaitu melanjutkan peruabahan         atau tidak dan konfirmasi kedua menyimpan perubahan atau tidak. Disini proses pengimputan data sama seperti ketika menginput data untuk pasien baru namun               bedanya disini kolom yang ingin di ubah dataya dapat dipilih satu saja, tidak mengubah data di kolom lainnya

    c.	Kembali ke menu utama
        Kembali ke menu utama dimana di dalamnya terdapat konfirmasi yes (y) or no (n), penggunaan while loop dan if else statement sebagai fungsi anti-typo, jika typo         atau pilihan tidak ada dia akan kemabli ke konfirmasi.

4.	Delete ( Menghapus Data Pasien )
    Di dalam menu ini terdapat 2 opsi :
    a.	Hapus pasien
        Di menu ini, user dapat menghapus pasien berdasarkan kode id nya, lalu akan ada konfirmasi apakah user ingin menghapus apa tidak, jika jadi maka data akan di           hapus, jika tidak maka akan Kembali ke menu menghapus data pasien.

    b.	Kembali ke menu utama
        Kembali ke menu utama dimana di dalamnya terdapat konfirmasi yes (y) or no (n), penggunaan while loop dan if else statement sebagai fungsi anti-typo, jika typo         atau pilihan tidak ada dia akan kemabli ke konfirmasi.

5.	Exit Program
    Keluar program dimana di dalamnya terdapat konfirmasi yes (y) or no (n), penggunaan while loop dan if else statement sebagai fungsi anti-typo, jika typo atau           pilihan tidak ada dia akan kembali ke konfirmasi.
