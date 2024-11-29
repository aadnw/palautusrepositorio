KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        if kapasiteetti is None:
            self.kapasiteetti = KAPASITEETTI
        elif not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")  # heitin vaan jotain :D
        else:
            self.kapasiteetti = kapasiteetti

        if kasvatuskoko is None:
            self.kasvatuskoko = OLETUSKASVATUS
        elif not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("kapasiteetti2")  # heitin vaan jotain :D
        else:
            self.kasvatuskoko = kasvatuskoko

        self.lista = self._luo_lista(self.kapasiteetti)

        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        if n in self.lista:
            return True
        else:
            return False

    def lisaa(self, n):
        if self.alkioiden_lkm == 0:
            self.lista[0] = n
            self.alkioiden_lkm += 1
            return True

        if not self.kuuluu(n):
            self.lista[self.alkioiden_lkm] = n
            self.alkioiden_lkm += 1

            # ei mahdu enempää, luodaan uusi säilytyspaikka luvuille
            if self.alkioiden_lkm % len(self.lista) == 0:
                self.lista_taynna_luo_uusi()
            return True

        return False

    def lista_taynna_luo_uusi(self):
        uusi_lista = self.lista
        self.lista = self._luo_lista(self.alkioiden_lkm + self.kasvatuskoko)
        self.kopioi_lista(uusi_lista, self.lista)

    def poista(self, n):
        if self.kuuluu(n):
            self.lista.remove(n)
            self.alkioiden_lkm -= 1
            return True
        else:
            return False

    def kopioi_lista(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = self._luo_lista(self.alkioiden_lkm)

        for i in range(0, len(taulu)):
            taulu[i] = self.lista[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        lista_a = a.to_int_list()
        lista_b = b.to_int_list()

        for i in range(0, max(len(lista_b), len(lista_a))):
            x.lisaa(lista_a[i])
            x.lisaa(lista_b[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        lista_a = a.to_int_list()
        lista_b = b.to_int_list()

        for i in range(0, len(lista_a)):
            for j in range(0, len(lista_b)):
                if lista_a[i] == lista_b[j]:
                    y.lisaa(lista_b[j])

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        lista_a = a.to_int_list()
        lista_b = b.to_int_list()

        for i in range(0, len(lista_a)):
            z.lisaa(lista_a[i])

        for i in range(0, len(lista_b)):
            z.poista(lista_b[i])

        return z

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.lista[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos += str(self.lista[i])
                tuotos += ", "
            tuotos += str(self.lista[self.alkioiden_lkm - 1])
            tuotos += "}"
            return tuotos
