
from hewan.hewan import Hewan

class Kucing(Hewan):
    def __init__(self, bunyi, jumlah_kaki = 2):
        super().__init__(bunyi)
        self.jumlah_kaki = jumlah_kaki
    
    def kaki(self):
        print(f"Kakinya: {self.jumlah_kaki}")    
        
    def suara(self):
        print(f"Suara kucing: {self.bunyi}")