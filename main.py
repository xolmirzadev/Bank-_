# Mijoz classi
class Bank:
    def __init__(self, ism, manzil, mobil_raqam):
        self.ism = ism
        self.manzil = manzil
        self.mobil_raqam = mobil_raqam
        self.accounts = []

    def hisob_ochish(self, account):
        self.accounts.append(account)

    def hisobni_yopish(self, account):
        self.accounts.remove(account)
        
    def hisob_olish(self):
        return self.accounts

    def ism_olish(self):
        return self.ism

    def manzil_olish(self):
        return self.manzil

    def telefon_raqam_olish(self):
        return self.mobil_raqam


# Account classi
class Account:
    def __init__(self, hisob_raqam, balans):
        self.hisob_raqam = hisob_raqam
        self.balans = balans

    def saqlangan_mablag(self, miqdor):
        self.balans += miqdor

    def bekor_qilmoq(self, miqdor):
        if miqdor > self.balans:
            raise ValueError("Mablag'lar yetarli emas")
        else:
            self.balans -= miqdor

    def hisobni_olmoq(self):
        return self.balans

    def hisob_raqam_olmoq(self):
        return self.hisob_raqam



class Dagavor:
    def __init__(self, account, hisobga_olish, miqdor):
        self.account = account
        self.hisobga_olish = hisobga_olish
        self.miqdor = miqdor

    def a(self):
        if self.account.hisobni_olmoq() < self.miqdor:
            raise ValueError("Mablag'lar yetarli emas!")

        else:
            self.account.bekor_qilmoq(self.miqdor)
            self.hisobga_olish.saqlangan_mablag(self.miqdor)
