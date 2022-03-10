import PySimpleGUI as sg

import main
import quiz_engine
from quiz_engine import QuizEngine
from main import *

sg.theme('Black')

layout = [  [sg.Text('Klausimų Viktorina', size=(20, 1), font=("ariel", 20, "bold"), text_color=sg.YELLOWS[0],
                     justification='Center') ],
            [sg.Input(key='-IN-'), sg.Text(size=(12,1), key='-OUT-')],
            [sg.Button('Go'), sg.Button('Exit')]    ]

window = sg.Window('Klausimų Viktorina', layout)

while True:
    event, values = window.read()
    print(event, values)
    if event in (None, 'Exit'):
        break
    if event == 'Go':
        window['-OUT-'].update(values['IN'])
window.close()

klausimai = []

class QuizUI:

    def __init__(self, qiuiz_engine: QuizEngine) -> None:
        self.quiz = qiuiz_engine


    def display_question(self):
        qtekstas = self.quiz.sekantis_klausimas()
        klausimai.append(qtekstas)

print(klausimai)

