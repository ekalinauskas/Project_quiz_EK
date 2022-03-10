import random
from random import shuffle
from Questions_DB import Questions
from quiz_engine import QuizEngine
from quiz_UI import QuizInterface
from quiz_engine import Klausimas
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///Questions.db')
Session = sessionmaker(bind=engine)
session = Session()

visi_klausimai = []

#Sukuria 5 unikalius skaicius
parenkami_atsitiktiniai = random.sample(range(1, 6), 5)

for a in parenkami_atsitiktiniai:
    atsakymu_pasirinkimai = []
    questions_get = session.query(Questions).get(a)
    question = questions_get.question
    correct_answer = questions_get.answer_correct
    inc_answer1 = questions_get.answer_incorrect1
    inc_answer2 = questions_get.answer_incorrect2
    atsakymu_pasirinkimai.append(correct_answer)
    atsakymu_pasirinkimai.append(inc_answer1)
    atsakymu_pasirinkimai.append(inc_answer2)
    shuffle(atsakymu_pasirinkimai)
    new_question = Klausimas(question, correct_answer, atsakymu_pasirinkimai)
    visi_klausimai.append(new_question)

viktorina = QuizEngine(visi_klausimai)
viktorinos_ui = QuizInterface(viktorina)




