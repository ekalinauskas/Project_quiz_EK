from tkinter import Tk, Canvas, StringVar, Label, Radiobutton, Button, messagebox, ttk
from quiz_engine import QuizEngine
from ttkthemes import themed_tk as tk

THEME_COLOR = "gold"


class QuizInterface:

    def __init__(self, quiz_brain: QuizEngine) -> None:
        self.quiz = quiz_brain
        # Nustato tema
        self.window = tk.ThemedTk()
        self.window.get_themes()
        self.window.set_theme("elegance")
        self.window.title("Klausimų Viktorina")
        self.window.geometry("900x600")
        self.window['background'] = '#856ff8'
        # Rodyti pavadinima
        self.rodyti_pavadinima()

        # Klausimo lango forma Canvas programos lange atvaizduoti klausimui
        self.canvas = Canvas(width=900, height=250, bg="#856ff8", highlightthickness=0)
        self.question_text = self.canvas.create_text(450, 125, text="Question here", width=680, justify="center",
                                                     fill=THEME_COLOR, font=('Ariel', 20, 'italic'))
        self.canvas.grid(row=2, column=0, columnspan=2, pady=50)
        self.klausimo_rodymas()

        # StringVar funkcija atsakymu saugojimui
        self.atsakymas_zaidejo = StringVar()

        # Pasirinkimo mygtukai (radio buttons)
        self.pasirinkimai = self.radio_buttons()
        self.rodyti_pasirinkimus()

        # Parodo atsakymas teisingas ar ne
        self.feedback = Label(self.window, pady=10, font=("ariel", 15, "bold"), bg="#856ff8" )
        self.feedback.place(x=350, y=400)

        # Mygtukai
        self.mygtukai()

        # Mainloop
        self.window.mainloop()

    def rodyti_pavadinima(self):

        """Programos pavadinimas"""

        # App pavadimimas
        pavadinimas = Label(self.window, text="Klausimų Viktorina",
                      width=40, bg="blue", fg="white", justify="center", font=("ariel", 36, "bold"))

        pavadinimas.place(x=0, y=0)

    def klausimo_rodymas(self):

        """Klausimo atvaizdavimas"""

        klausimo_tekstas = self.quiz.sekantis_klausimas()
        self.canvas.itemconfig(self.question_text, text=klausimo_tekstas)

    def radio_buttons(self):

        """Sukurti pasirinkimo pazymimus mygtukus (radio buttons)"""

        pasirinkumu_sarasas = []

        # pirmo mygtuko vieta
        y_pos = 240

        # Pasirinkimu pridejimas i sarasa
        while len(pasirinkumu_sarasas) < 3:

            # mygtuko stilius ir atsakymo priskyrimas mygtukui
            pasirinkimo_mygtukas = Radiobutton(self.window, text="", variable=self.atsakymas_zaidejo,
                                               value='', font=("ariel", 14), bg="#856ff8")

            pasirinkumu_sarasas.append(pasirinkimo_mygtukas)

            # radio mygtuko vieta pagrindiniame lange
            pasirinkimo_mygtukas.place(x=400, y=y_pos)

            # sekanciu radio mygtuko atvaizdavimas pasirinktu atstumu nuo auksciau esancio
            y_pos += 40

        # radio mygtukas i pagrindini langa su visa informacija
        return pasirinkumu_sarasas

    def rodyti_pasirinkimus(self):

        """Rodyti tris pasirinkimus"""

        val = 0

        # rodyti visus tuscius radio mygtukus
        self.atsakymas_zaidejo.set(None)

        # looping per klausimo atsakymus, kurie bus priskirti radio mygtukams
        for pasirinkimas in self.quiz.pateikiamas_klausimas.pasirinkimai:
            self.pasirinkimai[val]['text'] = pasirinkimas
            self.pasirinkimai[val]['value'] = pasirinkimas
            val += 1

    def next_btn(self):

        """Tikrina ar atsakymas teisingas ir ar nebuvo paskutinis klausimas"""

        # tikrinamas atsakymas
        if self.quiz.tikrinti(self.atsakymas_zaidejo.get()):
            self.feedback["fg"] = "green"
            self.feedback["text"] = 'Atsakymas teisingas! \U0001F44D'
        else:
            self.feedback['fg'] = 'darkred'
            self.feedback['text'] = ('\u274E Neteisingai! \n'
                                     f'Teisingas atsakymas: {self.quiz.pateikiamas_klausimas.teisingas_atsakymas}')

        if self.quiz.ar_paskutinis_klausimas():
            #Pereina prie sekancio klausimo
            self.klausimo_rodymas()
            self.rodyti_pasirinkimus()
        else:
            # jei nera daugiau klausimu rodo rezultata
            self.rezultatas()

            self.window.destroy()

    def mygtukai(self):

        """Kitas ir isieti mygtukai"""

        # mygtukas kitas
        kitas_mygtukas = Button(self.window, text="Kitas", command=self.next_btn,
                             width=10, bg="blue", fg="white", font=("ariel", 16, "bold"))

        # mygtuko vieta
        kitas_mygtukas.place(x=370, y=360)

        # Mygtukas uzdaryti programai
        iseiti_button = Button(self.window, text="Išeiti", command=self.window.destroy,
                             width=5, bg="red", fg="white", font=("ariel", 16, " bold"))

        iseiti_button.place(x=800, y=50)

    def rezultatas(self):

        """rezultatas iššokančiame lange"""

        taskai, neteisingai, procentai = self.quiz.tasku_skaiciavimas()

        taskai = f"Teisingai: {taskai}"
        neteisingai = f"Neteisingai: {neteisingai}"

        # procentinis rezultatas
        rezultatas = f"Atsakyta: {procentai}%"

        # "message box"
        messagebox.showinfo("Rezultatas", f"{rezultatas}\n{taskai}\n{neteisingai}")