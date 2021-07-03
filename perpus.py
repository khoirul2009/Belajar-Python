import os
from sys import executable
buku = ["matematika", "ips", "progaming", "anak rantau", "memasak", "manfaat jagung"]
def layarbersih(msg):
    input(msg)
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")
def mainMenu(x):
    if x == "1":
        listBuku()
    elif x == "2":
        judul = input("masukan judul buku : ")
        create(judul)
    elif x == "3":
        judul = input("input judul yang dicari : ")
        readone(judul)
    elif x == "4":
        judul = input("input judul yang dicari : ")
        delete(judul)
    elif x == "5":
        print("progam shutting down...")
    else:
        print("option not found")
def create(judul):
    buku.append(judul)
    layarbersih("buku berhasil ditambahkan, press any key to continue...")
def listBuku():
    print("Daftar buku..")
    no = 1
    for i in buku:
        print(str(no)+". "+ i)
        no += 1
    layarbersih("press any key...")
def delete(judul):
    if buku.count(judul) >= 1:
        buku.remove(judul)
        layarbersih("buku berhasil dihapus, press any key to continue...")
    else:
        layarbersih("buku tidak ditemukan")
def readone(judul):
    filteropject = filter(lambda a: judul in a, buku)
    p =  list(filteropject)
    if(not p):
        layarbersih("data tidak ditemukan, press any key to continue...")
    else:
        layarbersih("buku berjudul '" + ",".join(p)+"' berhasil ditemukan, press any key to continue...")

x = "0"
while x != "5":
    print("progam invetaris perpustakaan")
    print("[1] tampilkan semua buku")
    print("[2] tambahkan data buku")
    print("[3] cari data buku")
    print("[4] hapus data buku")
    print("[5] exit")

    x = input("pilihlah menu : ")
    mainMenu(x)
