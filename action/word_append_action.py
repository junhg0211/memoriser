from datetime import datetime

from action import Action
from database import Database
from word import Word


class WordAppendAction(Action):
    name = "단어 추가"

    def __init__(self, database: Database):
        self.database = database

    def tick(self):
        while True:
            word_raw = input("단어 > ").strip()
            meaning = input("의미 > ").strip()

            double_check = input("맞습니까? [y] > ")

            if double_check.lower().startswith("y"):
                break

        word = Word(word_raw, meaning, datetime.now().timestamp())
        self.database.push_word(word)
