class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros

    def kerros_ylös(self):
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros += 1
            print(f"Hissi on nyt kerroksessa {self.nykyinen_kerros}")

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1
            print(f"Hissi on nyt kerroksessa {self.nykyinen_kerros}")

    def siirry_kerrokseen(self, kohde_kerros):

        if kohde_kerros < self.alin_kerros or kohde_kerros > self.ylin_kerros:
            print(f"Kohdekerros {kohde_kerros} on hissin sallittujen kerrosten ulkopuolella.")
            return

        while self.nykyinen_kerros < kohde_kerros:
            self.kerros_ylös()
        while self.nykyinen_kerros > kohde_kerros:
            self.kerros_alas()


class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lkm):
        self.hissit = [Hissi(alin_kerros, ylin_kerros) for _ in range(hissien_lkm)]

    def aja_hissiä(self, hissin_numero, kohde_kerros):
        if 0 <= hissin_numero < len(self.hissit):
            print(f"Ajetaan hissiä {hissin_numero + 1} kerrokseen {kohde_kerros}")
            self.hissit[hissin_numero].siirry_kerrokseen(kohde_kerros)
        else:
            print(f"Hissiä numero {hissin_numero} ei ole olemassa.")


talo = Talo(1, 5, 3)

talo.aja_hissiä(0, 3)
talo.aja_hissiä(1, 5)
talo.aja_hissiä(2, 1)
