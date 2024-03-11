from dataclasses import asdict
from os.path import isfile
from json import load, dump

from word import Word


class Database:
    def __init__(self, filename: str):
        self.filename = filename

        self.words = list()

        if isfile(self.filename):
            self.load()
        else:
            self.save()

    def push_word(self, word):
        self.words.append(word)
        self.save()

    def load(self):
        with open(self.filename, "r", encoding="utf-8") as file:
            raw_data = load(file)

        # -- load words
        self.words.clear()
        for raw_word in raw_data["words"]:
            self.words.append(Word(**raw_word))

    def save(self):
        raw_data = dict()

        # -- pack words
        words = list()
        for word in self.words:
            words.append(asdict(word))
        raw_data["words"] = words

        # -- dump data
        with open(self.filename, "w", encoding="utf-8") as file:
            dump(raw_data, file, sort_keys=True, ensure_ascii=False)
