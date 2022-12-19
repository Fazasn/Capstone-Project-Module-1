
# Capstone Project Module 1 Faza Syafri Nur Rahman _ JCDS - 1904 -015


ListPasien = {
    "PSN001":{
        'Nama': ' Riza Santoso ',
        'Umur': 25,
        'Jenis Kelamin' : 'Pria\t',
        'Goldar' : 'A',
        'Alamat': 'Jakarta',
        'Status Pasien': 'Rawat Jalan'
    },
    "PSN002":{
        'Nama': ' Abu Haekal S ',
        'Umur': 35,
        'Jenis Kelamin' : 'Pria\t',
        'Goldar' : 'B',
        'Alamat': 'Jakarta',
        'Status Pasien': 'Rawat Jalan'
    },
    "PSN003":{
        'Nama': ' Eko Yulianto ',
        'Umur': 50,
        'Jenis Kelamin': 'Pria\t',
        'Goldar' : 'A',
        'Alamat': 'Cilacap',
        'Status Pasien': 'Rawat Jalan'
    },
    "PSN004":{
        'Nama': ' Dwi Retnosari',
        'Umur': 23,
        'Jenis Kelamin': 'Wanita',
        'Goldar' : 'O',
        'Alamat': 'Cirebon',
        'Status Pasien': 'Rawat Inap'
    },
    "PSN005":{
        'Nama': ' Ajeng Fauziah',
        'Umur': 27,
        'Jenis Kelamin': 'Wanita',
        'Goldar' : 'AB',
        'Alamat': 'Cirebon',
        'Status Pasien': 'Rawat Inap'
    }
}

kolomupdate=['Nama','Umur','Jenis Kelamin','Goldar','Alamat','Status Pasien']


def DataPasien(): 
    while True: 
        print('''
        ==================== List Menu Data Pasien : ====================

        1. Tampilkan Semua Data
        2. Tampilkan Data Pasien Berdasarkan Kode Pasien
        3. Tampilkan Data Pasien Berdasarkan Nama
        4. Tampilkan Data Pasien Sesuai Status
        5. Kembali ke Menu Sebelumnya

        ===================================================================
        ''')

        kodepilihan=input('\n Masukkan Angka Menu Yang Ingin Dijalankan: ')
        if kodepilihan == '1':
            if ListPasien != '':
                print('\n ============================================================ Data Pasien ============================================================ \n')
                print('ID_Pasien \t| Nama  \t\t| Umur \t| Jenis Kelamin\t | Golongan Darah |\t Alamat \t| \tStatus Pasien')
                for index in ListPasien:
                    print(f'{index}\t\t|', f'{ListPasien[index]["Nama"]}\t|', f'{ListPasien[index]["Umur"]}\t|', f'{ListPasien[index]["Jenis Kelamin"]}\t', f'|\t{ListPasien[index]["Goldar"]}\t ', f'|\t{ListPasien[index]["Alamat"]}\t\t|', f'\t{ListPasien[index]["Status Pasien"]}')
            else:
                print('========== Tidak Ada Data Pasien ==========')

        elif kodepilihan == '2':
            if ListPasien != '':
                kodepasien=input('\nMasukkan Kode ID Pasien Yang Ingin Ditampilkan : ').upper()
                if kodepasien in ListPasien:
                    print('\n ============================================================ Data Pasien ============================================================ \n')
                    print('ID_Pasien \t| Nama  \t\t| Umur \t| Jenis Kelamin\t | Golongan Darah |\t Alamat \t| \tStatus Pasien')
                    print(f'{kodepasien}\t\t|', f'{ListPasien[kodepasien]["Nama"]}\t|', f'{ListPasien[kodepasien]["Umur"]}\t|', f'{ListPasien[kodepasien]["Jenis Kelamin"]}\t', f'|\t{ListPasien[kodepasien]["Goldar"]}\t ', f'|\t{ListPasien[kodepasien]["Alamat"]}\t\t|', f'\t{ListPasien[kodepasien]["Status Pasien"]}')
                else:
                    print('\n ========== Data Pasien Tidak Ditemukan ==========')        
            else:
                print('\n ========== Tidak Ada Data Pasien ==========')

        elif kodepilihan == '3':
            if ListPasien != '':
                namapasien=input('\nMasukkan Nama Pasien Yang Ingin Ditampilkan : ').title()
                count = 0
                for key in ListPasien.keys():
                    if namapasien in ListPasien[key]['Nama']:
                        count += 1
                        print('\n ============================================================ Data Pasien ============================================================ \n')
                        print('ID_Pasien \t| Nama  \t\t| Umur \t| Jenis Kelamin\t | Golongan Darah |\t Alamat \t| \tStatus Pasien')
                        print(f'{key}\t\t|', f'{ListPasien[key]["Nama"]}\t|', f'{ListPasien[key]["Umur"]}\t|', f'{ListPasien[key]["Jenis Kelamin"]}\t', f'|\t{ListPasien[key]["Goldar"]}\t ', f'|\t{ListPasien[key]["Alamat"]}\t\t|', f'\t{ListPasien[key]["Status Pasien"]}')
                    else:
                        count += 0
                if count == 0:
                    print('\n ========== Data Tidak Ditemukan ==========')
            else:
                print('\n ========== Tidak Ada Data Pasien ==========')

        elif kodepilihan == '4':
            if ListPasien != '':
                while True:
                    StatusPasien=input('\nMasukkan Status Pasien Yang Anda Ingin Lihat ( Rawat Inap / Rawat Jalan ) : ').title()    
                    if StatusPasien == 'Rawat Inap' or StatusPasien == 'Rawat Jalan':
                        break
                    else:
                        print('\n Hanya Input Rawat Inap atau Rawat Jalan')

                count=0
                for key in ListPasien.keys():
                    if StatusPasien in ListPasien[key]['Status Pasien']:
                        count+=1
                        print('\n ============================================================ Data Pasien ============================================================ \n')
                        print('ID_Pasien \t| Nama  \t\t| Umur \t| Jenis Kelamin\t | Golongan Darah |\t Alamat \t| \tStatus Pasien')
                        print(f'{key}\t\t|', f'{ListPasien[key]["Nama"]}\t|', f'{ListPasien[key]["Umur"]}\t|', f'{ListPasien[key]["Jenis Kelamin"]}\t', f'|\t{ListPasien[key]["Goldar"]}\t ', f'|\t{ListPasien[key]["Alamat"]}\t\t|', f'\t{ListPasien[key]["Status Pasien"]}')
                    else:
                        count+=0
                if count ==0:
                    print('\n ========== Data Tidak Ditemukan ==========')                
            else:
                print('\n ========== Tidak Ada Data Pasien ==========')

        elif kodepilihan == '5':
                while True:
                    konfirmasi=input('\n Apakah Anda Yakin Ingin Keluar dari Menu ini? Y / N :')
                    if konfirmasi.lower() == 'y':
                        print('\n ========== Anda Kembali ke Menu Utama ==========')
                        break
                    elif konfirmasi.lower() == 'n':
                        DataPasien()
                        break
                    else:
                        print('\n ========== Masukkan Input yang Benar ==========')
                break
        
        else:
            print('\n ========== Mohon Masukkan Input yang Benar ==========')

def TambahPasien():
    while True:
        print('''
        ==================== List Menu Tambah Pasien : ====================

        1. Tambah Data Pasien
        2. Kembali Ke Menu Sebelumnya

        ===================================================================
        ''')

        kodepilihan=input('\n Masukkan Angka Menu Yang Ingin Dijalankan: ')
        if kodepilihan == '1':
            while True:
                while True:
                    nomorpasien=input('\n Masukkan NOMOR Kode untuk Pasien Baru : ')
                    if nomorpasien.isdigit() == False:
                        print('\n========= Masukkan Hanya ANGKA =========')
                    else:
                        kodepasien='PSN'+nomorpasien
                        if kodepasien in ListPasien:
                            print('\n ========== Kode Sudah Terpakai, Masukkan Kode Baru ==========')
                        else:
                            print('\n ========== Kode Dapat Digunakan ==========')
                            break   

                Nama = input('\n Masukkan Nama Pasien : ')
                
                while True:
                    UmurInput = input('\n Masukkan Umur Pasien : ')
                    if UmurInput.isdigit() == False:
                        print('\n========= Masukkan Hanya ANGKA =========')
                    else:
                        Umur=int(UmurInput)
                        if Umur < 0:
                            print('\n Mohon Masukkan Umur yang Benar ')
                        else:
                            break
                
                while True:
                    Jenis_Kelamin = input('\n Masukkan Jenis Kelamin Pasien : ').capitalize()
                    if Jenis_Kelamin == 'Pria' or Jenis_Kelamin == 'Wanita':
                        break
                    else:
                        print('\n Masukkan Hanya Pria atau Wanita')
                
                while True:
                    Goldar = input('\n Masukkan Golongan Darah Pasien : ').upper()
                    if Goldar == 'A' or Goldar=='B' or Goldar=='AB' or Goldar=='O':
                        break
                    else:
                        print('\n Masukkan Hanya Golongan Darah A, B, AB, O')

                Alamat_Baru = input('\n Masukkan Alamat Pasien : ').title()

                while True:
                    StatusBaru = input('\n Masukkan Status Pasien : ').title()
                    if StatusBaru == 'Rawat Inap' or StatusBaru=='Rawat Jalan':
                        break
                    else:
                        print('\n Masukkan Hanya Rawat Inap atau Rawat Jalan')

                print('\n ============================================================ Data Pasien ============================================================ \n')
                print('ID_Pasien \t| Nama  \t\t| Umur \t| Jenis Kelamin\t | Golongan Darah |\t Alamat \t| \tStatus Pasien')
                print(f'{kodepasien}\t\t|', f'{Nama}\t|', f'{Umur}\t|', f'{Jenis_Kelamin}\t', f'|\t{Goldar}\t ', f'|\t{Alamat_Baru}\t\t|', f'\t{StatusBaru}')

                while True:
                    konfirmasi=input('\n Apakah anda ingin menyimpan data pasien ini? Y / N : ')
                    if konfirmasi.lower() == 'y':
                        ListPasien.update({
                        str(kodepasien):{
                        'Nama':  Nama,
                        'Umur': Umur,
                        'Jenis Kelamin': Jenis_Kelamin,
                        'Goldar' : Goldar,
                        'Alamat' : Alamat_Baru,
                        'Status Pasien' : StatusBaru
                        }})
                        print('\n ========== Data Pasien Baru sudah Tersimpan ==========\n')
                        break
                    elif konfirmasi.lower() == 'n':
                        print('\n========== Data Pasien Tidak Disimpan ==========') 
                        break
                    else:
                        print('\n========== Mohon Masukkan Input yang Benar ==========\n')
                break

        elif kodepilihan == '2':
            while True:
                kodeinput=input('\n Apakah Anda Yakin Ingin Keluar Dari Menu Ini? Y / N ')
                if kodeinput.lower() == 'y':
                    print('\n ========== Anda Kembali ke Menu Utama ==========')
                    break
                elif kodeinput.lower() == 'n':
                    TambahPasien()
                    break
                else:
                    print('\n========== Mohon Masukkan Input yang Benar ==========')
            break 
        else:
            print('\n========== Mohon Masukkan Input yang Benar ==========')

def UpdatePasien():
    while True:
        print('''
        ==================== List Menu Update Pasien : ====================

        1. Ubah Data Pasien Menyeluruh
        2. Ubah Data Pasien Sesuai Kolom
        3. Kembali Ke Menu Sebelumnya

        ===================================================================
        ''')

        kodepilihan=input('\n Masukkan Angka Menu Yang Ingin Dijalankan: ')
        if kodepilihan == '1':
            kodepasien=input('\n Masukkan Kode Pasien Yang Akan Diubah Datanya: ').upper()  
            if kodepasien in ListPasien:
                    print('\n ========== Data Pasien Ditemukan ==========')
                    print('\n ============================================================ Data Pasien ============================================================ \n')
                    print('ID_Pasien \t| Nama  \t\t| Umur \t| Jenis Kelamin\t | Golongan Darah |\t Alamat \t| \tStatus Pasien')
                    print(f'{kodepasien}\t\t|', f'{ListPasien[kodepasien]["Nama"]}\t|', f'{ListPasien[kodepasien]["Umur"]}\t|', f'{ListPasien[kodepasien]["Jenis Kelamin"]}\t', f'|\t{ListPasien[kodepasien]["Goldar"]}\t ', f'|\t{ListPasien[kodepasien]["Alamat"]}\t\t|', f'\t{ListPasien[kodepasien]["Status Pasien"]}')
                    
                    while True:
                        lanjut=input('\n Apakah Anda Yakin Ingin Melanjutkan Perubahan Data? Y / N : ')
                        if lanjut.lower() == 'y':
                            namabaru = input('\n Masukkan Perubahan Nama Pasien : ')

                            while True:
                                UmurInput = input('\n Masukkan Umur Pasien : ')
                                if UmurInput.isdigit() == False:
                                    print('\n========= Masukkan Hanya ANGKA =========')
                                else:
                                    umurbaru=int(UmurInput)
                                    if umurbaru < 0:
                                        print('\n Mohon Masukkan Umur yang Benar ')
                                    else:
                                        break

                            while True:
                                jenis_kelamin_baru = input('\n Masukkan Perubahan Jenis Kelamin Pasien : ').capitalize()
                                if jenis_kelamin_baru == 'Pria' or jenis_kelamin_baru == 'Wanita':
                                    break
                                else:
                                    print('\n========== Masukkan Hanya Pria atau Wanita ==========')
            
                            while True:
                                goldarbaru = input('\n Masukkan Perubahan Golongan Darah Pasien :  ').upper()
                                if goldarbaru == 'A' or goldarbaru=='B' or goldarbaru=='AB' or goldarbaru=='O':
                                    break
                                else:
                                    print('\n Masukkan Hanya Golongan Darah A, B, AB, O')

                            alamatbaru = input('\n Masukkan Perubahan Alamat Pasien : ')

                            while True:
                                statusbaru = input('\n Masukkan Status Baru Pasien : ').title()
                                if statusbaru == 'Rawat Inap' or statusbaru=='Rawat Jalan':
                                    break
                                else:
                                    print('\n Masukkan Hanya "Rawat Inap" atau "Rawat Jalan"')

                            print('\n ============================================================ Data Pasien ============================================================ \n')
                            print('Nama  \t\t| Umur \t| Jenis Kelamin\t | Golongan Darah |\t Alamat \t| \tStatus Pasien')
                            print(f'{namabaru}\t', f'{umurbaru}\t', f'{jenis_kelamin_baru}\t', f'{goldarbaru}\t', f'{alamatbaru}', f'{statusbaru}')
                            
                            while True:
                                konfirmasi=input('\n Apakah Anda Ingin Menyimpan Data Pasien Ini? Y / N : ')
                                if konfirmasi.lower() == 'y':
                                    ListPasien.update(
                                    {kodepasien:{
                                        'Nama': namabaru,
                                        'Umur': umurbaru,
                                        'Jenis Kelamin' : jenis_kelamin_baru,
                                        'Goldar' : goldarbaru,
                                        'Alamat': alamatbaru,
                                        'Status Pasien' : statusbaru
                                        }})
                                    print('\n========== Data Pasien Sudah Diperbaharui ==========\n')
                                    break

                                elif konfirmasi.lower() == 'n':
                                    print('\n========== Data Pasien Tidak Diperbaharui ==========\n') 
                                    break
                                else:
                                    print('\n========== Masukkan Input yang Benar ==========\n')
                            break

                        elif lanjut.lower() == 'n':
                            print('\n========== Anda Tidak Melanjutkan Pembaharuan ==========') 
                            break

                        else:
                            print('\n========== Mohon Masukkan Input yang Benar ==========\n')

            else:
                    print('\n========== Data Pasien Tidak Ditemukan ==========')

        elif kodepilihan == '2': 
            kodepasien=input('\n Masukkan Kode Pasien Yang Akan Diubah Datanya: ').upper()
            if kodepasien in ListPasien:
                print('\n ========== Data Pasien Ditemukan ==========')
                print('\n ============================================================ Data Pasien ============================================================ \n')
                print('ID_Pasien \t| Nama  \t\t| Umur \t| Jenis Kelamin\t | Golongan Darah |\t Alamat \t| \tStatus Pasien')
                print(f'{kodepasien}\t\t|', f'{ListPasien[kodepasien]["Nama"]}\t|', f'{ListPasien[kodepasien]["Umur"]}\t|', f'{ListPasien[kodepasien]["Jenis Kelamin"]}\t', f'|\t{ListPasien[kodepasien]["Goldar"]}\t ', f'|\t{ListPasien[kodepasien]["Alamat"]}\t\t|', f'\t{ListPasien[kodepasien]["Status Pasien"]}')
                
                while True:
                    lanjut=input('\n Apakah Anda Yakin Ingin Melanjutkan Perubahan Data? Y / N : ')
                    if lanjut.lower() == 'y':
                        while True:
                            print('''

                            Kolom Update Yang Dapat Diubah:

                            Nama | Umur | Jenis Kelamin | Goldar | Alamat | Status Pasien
                            
                            * Hanya Masukkan Nama Satu Kolom Pada Saat Input *
                            
                            ''')
                            kolomuser=input('\n Masukkan Nama Kolom Yang Ingin Di Ubah : ')
                            if kolomuser.title() in kolomupdate:
                                if kolomuser.title() == 'Nama':
                                    inputuser=input('\n Masukkan Perubahan Nama Pasien : ').title()
                                    print(f'\n{inputuser}')

                                elif kolomuser.title() == 'Umur':
                                    while True:
                                        UmurInput = input('\n Masukkan Umur Pasien : ')
                                        if UmurInput.isdigit() == False:
                                            print('\n========= Masukkan Hanya ANGKA =========')
                                        else:
                                            inputuser=int(UmurInput)
                                            if inputuser < 0:
                                                print('\n Mohon Masukkan Umur yang Benar ')
                                            else:
                                                break
                                    print(f'{inputuser}\t')

                                elif kolomuser.title() == 'Jenis Kelamin':
                                    while True:
                                        inputuser = input('\nMasukkan Jenis Kelamin Pasien : ').capitalize()
                                        if inputuser == 'Pria' or inputuser == 'Wanita':
                                            break
                                        else:
                                            print('\nMasukkan Hanya Pria atau Wanita')

                                    print(f'{inputuser}\t')

                                elif kolomuser.title() == 'Goldar':
                                    while True:
                                        inputuser = input('\nMasukkan Golongan Darah Pasien :  ').upper()
                                        if inputuser == 'A' or inputuser=='B' or inputuser=='AB' or inputuser=='O':
                                            break
                                        else:
                                            print('\nMasukkan Hanya Golongan Darah A, B, AB, O')

                                    print(f'{inputuser}\t')

                                elif kolomuser.title() == 'Alamat':
                                    inputuser = input('\n Masukkan Perubahan Alamat Pasien : ')
                                    print(f'{inputuser}')

                                elif kolomuser.title() == 'Status Pasien':
                                    while True:
                                        inputuser = input('\nMasukkan Status Baru Pasien :  ').title()
                                        if inputuser == 'Rawat Jalan' or inputuser=='Rawat Inap':
                                            break
                                        else:
                                            print('\nMasukkan Hanya "Rawat Jalan" atau "Rawat Inap"')

                                    print(f'{inputuser}\t')
                                break
                            else:
                                print('\n========== Kolom Tidak Ada ==========')

                        while True:
                            konfirmasi=input('\nApakah Anda Ingin Menyimpan Data Pasien Ini? Y / N : ')
                            if konfirmasi.lower() == 'y':
                                ListPasien[kodepasien][kolomuser.title()]=inputuser
                                print('\n========== Data Pasien Sudah Diperbaharui ==========')
                                break
                            elif konfirmasi.lower() == 'n':
                                print('\n========== Data Pasien Tidak Diperbaharui ==========')
                                break
                            else:
                                print('\n========== Masukkan Input yang Benar ==========')
                        break      
                            

                    elif lanjut.lower() == 'n':
                        print('\n========== Anda Tidak Melanjutkan Perubahan Data ==========')
                        break
                    else:
                        print('\n========== Mohon Masukkan Input Yang Benar ==========')
            else:
                print('\n========== Data Pasien Tidak Ditemukan : ==========')

        elif kodepilihan == '3':
                while True:
                    konfirmasi=input('\n Apakah Anda Yakin Mau Keluar Dari Menu Ini? Y / N : ')
                    if konfirmasi.lower() == 'y':
                        print('\n========== Anda Kembali ke Menu Sebelumnya ==========')
                        break
                    elif konfirmasi.lower() == 'n':
                        UpdatePasien()
                        break
                    else:
                        print('\n========== Mohon Masukkan Input yang Benar ==========')
                break

        else:
            print('\n========== Mohon Masukkan Input yang Benar ==========')


def HapusPasien():
    while True:
        print('''
        ==================== List Menu Hapus Pasien : ====================

        1. Hapus Data Pasien 
        2. Kembali Ke Menu Sebelumnya

        ==================================================================
        ''')


        kodepilihan=input('\n Masukkan Angka Menu Yang Ingin Dijalankan: ')
        if kodepilihan == '1':
            kodepasien=input('\n Masukkan Kode Pasien Yang Ingin Dihapus: ').upper()
            if kodepasien in ListPasien:
                print('\n========== Data Pasien Ditemukan ==========')
                print('\n========== Data Pasien ==========')
                print('ID_Pasien \t| Nama  \t\t| Umur \t| Jenis Kelamin\t | Golongan Darah |\t Alamat \t| \tStatus Pasien')
                print(f'{kodepasien}\t\t|', f'{ListPasien[kodepasien]["Nama"]}\t|', f'{ListPasien[kodepasien]["Umur"]}\t|', f'{ListPasien[kodepasien]["Jenis Kelamin"]}\t', f'|\t{ListPasien[kodepasien]["Goldar"]}\t ', f'|\t{ListPasien[kodepasien]["Alamat"]}\t\t|', f'\t{ListPasien[kodepasien]["Status Pasien"]}')
                
                while True:    
                    Konfirmasi=input('\n Apakah Anda Yakin Ingin Menghapus Data Pasien Ini? Y / N : ')
                    if Konfirmasi.lower() == 'y':
                        del ListPasien[kodepasien]
                        print('\n ========== Data Pasien Berhasil Dihapus ==========')
                        break
                    elif Konfirmasi.lower() == 'n':
                        print('\n========== Data Pasien Batal Dihapus ==========')
                        break
                    else:
                        print('\n========== Mohon Masukkan Input yang Benar ==========')            
            else:
                print('\n========== Data Pasien Tidak Ada / Sudah Dihapus ==========')
            
            

        elif kodepilihan == '2':
            while True:
                kodeinput=input('\n Apakah Anda Yakin Ingin Keluar dari Program? Y / N ')
                if kodeinput.lower() == 'y':
                    print('\n ========== Anda Kembali Ke Menu Utama ========== \n')
                    break
                elif kodeinput.lower() == 'n':
                    HapusPasien()
                    break
                else:
                    print('\n ========== Mohon Masukkan Input yang Benar ==========\n')
            break
            

        else:
            print('\n========== Mohon Masukkan Input yang Benar ==========')


def MainMenu():
    while True:
        print('''
        ==================== Selamat Datang di Mini Application RS ====================
        
        List Menu:
        1. Menampilkan Daftar Pasien
        2. Menambah Daftar Pasien
        3. Memperbaharui Daftar Pasien
        4. Hapus Data
        5. Exit Program 

        ===============================================================================
        ''')

        kodepilihan=input('\n Masukkan Angka Menu Yang Ingin Dijalankan: ')

        if kodepilihan == '1':
            DataPasien()

        elif kodepilihan == '2':
            TambahPasien()

        elif kodepilihan == '3':
            UpdatePasien()

        elif kodepilihan == '4':
            HapusPasien()
            
        elif kodepilihan == '5':
            while True:
                kodeinput=input('\n Apakah Anda Yakin Ingin Keluar dari Program? Y / N ')
                if kodeinput.lower() == 'y':
                    print('\n ========== Terima Kasih Telah Menggunakan Mini Application RS ========== \n')
                    break
                elif kodeinput.lower() == 'n':
                    MainMenu()
                    break
                else:
                    print('\n ========== Mohon Masukkan Input yang Benar ==========\n')
            break
        else:
            print('\n ========== Pilihan Yang Anda Masukkan Salah ========== \n')

MainMenu()