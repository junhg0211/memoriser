from datetime import timedelta, datetime
from random import random, shuffle

from action import Action


def recap_duration(recap_count: int) -> timedelta:
    return timedelta(hours=6) * 2**recap_count


class RecapAction(Action):
    name = "단어 복습"

    def __init__(self, database):
        super().__init__()

        self.database = database

    def tick(self):
        now = datetime.now()

        recap_count = 0
        correct_count = 0
        next_recap_time = None
        shuffle(self.database.words)
        for word in self.database.words:
            recap_threshold = word.get_recapped_date() + recap_duration(
                word.recap_count
            )

            # update next recap time
            if next_recap_time is None or recap_threshold < next_recap_time:
                next_recap_time = recap_threshold

            # if not recap word
            if recap_threshold > now:
                continue

            # make question
            meaning_recap = random() < 0.5
            if meaning_recap:
                print(f"의미: {word.meaning}")
            else:
                print(f"단어: {word.word}")
            input("> ")

            print(word)

            # check correct or not
            while True:
                is_correct = input("맞았습니까? [y/n] > ").lower()

                if is_correct.startswith("y"):
                    word.recapped_date = now.timestamp()
                    word.recap_count += 1
                    correct_count += 1
                    break

                if is_correct.startswith("n"):
                    word.recapped_date = 0.0
                    word.recap_count = 0
                    break

            recap_count += 1

        # print result
        if recap_count:
            print(f"총 {recap_count}개의 단어를 복습했습니다.")
            print(f"그 중에 {correct_count}개의 단어를 맞췄습니다.")
            print(f"점수는 {correct_count / recap_count * 100:,.2f}점입니다.")
        else:
            print("복습할 단어가 없습니다.")

        self.database.save()
