
class Klausimas:
    def __init__(self, klausimas: str, teisingas_atsakymas: str, pasirinkimai: list):
        self.klausimo_tekstas = klausimas
        self.teisingas_atsakymas = teisingas_atsakymas
        self.pasirinkimai = pasirinkimai


class QuizEngine:

    def __init__(self, klausimai):
        self.klausimas_nr = 0
        self.taskai = 0
        self.klausimai = klausimai
        self.pateikiamas_klausimas = None


    def sekantis_klausimas(self):

        """Pereiti prie sekancio klausimo ir paruosti pateikiamo klausimo formata"""

        self.pateikiamas_klausimas = self.klausimai[self.klausimas_nr]
        self.klausimas_nr += 1
        klausimo_tekstas = self.pateikiamas_klausimas.klausimo_tekstas
        return f"Klausimas Nr. {self.klausimas_nr}\n {klausimo_tekstas}"

    def tikrinti(self, user_answer):

        """Tikrina ar atsakymas teisingas, skaiciuoja teisingu atsakymu taskus"""

        teisingas_atsakymas = self.pateikiamas_klausimas.teisingas_atsakymas
        if user_answer.lower() == teisingas_atsakymas.lower():
            self.taskai += 1
            return True
        else:
            return False

    def tasku_skaiciavimas(self):

        """Grazina teisingu, neteisingu atsakymu skaiciu, parodo procentus"""

        neteisingai = self.klausimas_nr - self.taskai
        procentai = int(self.taskai / self.klausimas_nr * 100)
        return (self.taskai, neteisingai, procentai)

    def ar_paskutinis_klausimas(self):

        """tikrina ar dar bus klausimu"""

        return self.klausimas_nr < len(self.klausimai)
