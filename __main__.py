from dataclasses import dataclass, asdict
from datetime import datetime
from json import load, dump
from os.path import isfile


@dataclass
class Word:
    word: str
    meaning: str
    added_date: float
    recapped_date: float = 0.0

    def get_added_date(self) -> datetime:
        return datetime.fromtimestamp(self.added_date)

    def get_recappted_date(self) -> datetime:
        return datetime.fromtimestamp(self.recapped_date)


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


class Action:
    name = ""

    def __init__(self):
        assert self.name

    def tick(self):
        pass


class QuitAction(Action):
    name = "프로그램 종료"

    def __init__(self, quit_function):
        super().__init__()

        self.quit = quit_function

    def tick(self):
        self.quit()


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


class Frame:
    def __init__(self):
        self.running = True

        self.database = Database("database.json")

        self.actions = list()
        self.actions.append(QuitAction(self.quit))
        self.actions.append(WordAppendAction(self.database))

    def tick(self):
        # -- print title page
        print("=== MEMORISER")
        print()
        for i, action in enumerate(self.actions):
            print(f"{i+1}. {action.name}")
        print()
        action_number = input("> ")

        # -- check action_number validity
        try:
            action_number = int(action_number)
        except ValueError:
            print("다시 입력해주세요.")
            return

        if action_number < 0 or action_number > len(self.actions):
            print("다시 입력해주세요.")
            return

        # -- invoke action
        action = self.actions[action_number - 1]
        action.tick()

    def quit(self):
        self.running = False

    def run(self):
        while self.running:
            self.tick()


if __name__ == "__main__":
    frame = Frame()
    frame.run()
