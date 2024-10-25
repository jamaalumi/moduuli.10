import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdytä(self, muutos):
        self.nopeus += muutos
        if self.nopeus < 0:
            self.nopeus = 0
        elif self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus

    def kulje(self, tunti):
        self.matka += self.nopeus * tunti

class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            nopeuden_muutos = random.randint(-10, 15)
            auto.kiihdytä(nopeuden_muutos)
            auto.kulje(1)

    def tulosta_tilanne(self):
        print(f"{'Rekisteri':<10} {'Nopeus (km/h)':<15} {'Matka (km)':<10}")
        for auto in self.autot:
            print(f"{auto.rekisteritunnus:<10} {auto.nopeus:<15} {auto.matka:<10.1f}")
        print("-" * 40)

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.matka >= self.pituus:
                return True
        return False

# 
autot = [Auto(f"ABC-{i+1}", random.randint(100, 200)) for i in range(10)]
kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

tunti = 0
while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu()
    tunti += 1

    if tunti % 10 == 0:
        print(f"\nTilanne {tunti} tunnin jälkeen:")
        kilpailu.tulosta_tilanne()

print("\nKilpailu päättyi!")
kilpailu.tulosta_tilanne()
