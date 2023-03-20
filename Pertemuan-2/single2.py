class Manusia:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    def presentasi(self):
        print(f"{self.nama} sedang presentasi.")

class Dosen(Manusia):
    def __init__(self, nama, umur, nim):
        super().__init__(nama, umur)
        self.nim = nim
    def mengajar(self):
        print(f"{self.nama} dengan NIM {self.nim} sedang presentasi.")
dosenA = Dosen("Farhan Galih Pradana", 20, "210511090")
dosenA.presentasi() 
dosenA.mengajar() 