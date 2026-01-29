class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

    def tampilkan(self):
        print("Nama:", self.nama)
        print("NIM:", self.nim)

mhs = Mahasiswa("Mario", "11S25055")
mhs.tampilkan()
