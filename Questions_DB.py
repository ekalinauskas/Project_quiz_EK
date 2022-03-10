from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///Questions.db')
Base = declarative_base()


class Questions(Base):
    __tablename__ = 'Questions'
    id = Column(Integer, primary_key=True)
    question = Column('Klausimas', String)
    answer_correct = Column('Teisingas atsakymas', String)
    answer_incorrect1 = Column('1 Neteisingas atsakymas', String)
    answer_incorrect2 = Column('2 Neteisingas atsakymas', String)

    def __init__(self, question, answer_correct, answers_incorrect1, answers_incorrect2):
        self.question = question
        self.answer_correct = answer_correct
        self.answer_incorrect1 = answers_incorrect1
        self.answer_incorrect2 = answers_incorrect2

    def __repr__(self):
        return f'{self.id} {self.question} {self.answer_correct}'


Base.metadata.create_all(engine)
