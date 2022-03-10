from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Questions_DB import Questions


engine = create_engine('sqlite:///Questions.db')
Session = sessionmaker(bind=engine)
session = Session()


while True:
    options = int(input(""" Pasirinkite veiksmą:
    Įvesti naują klausimą - 1
    Išeiti iš programos - 2"""))
    if options == 1:
        question = input('Įveskite klausimą ')
        answer_correct = input('Įveskite teisingą atsakymą ')
        answer_incorrect1 = input('Įveskite pirmą neteisingą atsakymą ')
        answer_incorrect2 = input('Įveskite antrą neteisingą atsakymą ')
        question = Questions(question, answer_correct, answer_incorrect1, answer_incorrect2)
        session.add(question)
        session.commit()

    if options == 2:
        print("Viso gero")
        break


# Kuris pagoniškas lietuvių dievas dar vadinamas Poškučiu, Brazdeikiu, Dūdų Seniu?', 'Perkūnas', 'Patrimpas, Pikuolis')