from action import Action


def normalise(string: str) -> str:
    result = list()

    for letter in string:
        if letter in "1234567890":
            continue
        if letter == " ":
            continue
        result.append(letter.lower())

    return "".join(result)


class DictionaryAction(Action):
    name = "사전 보기"

    def __init__(self, database):
        super().__init__()
        self.database = database

    def tick(self):
        query = input("> ")
        normalised = normalise(query)

        matchings = list()
        for word in self.database.words:
            if normalised in normalise(word.word) or normalised in normalise(
                word.meaning
            ):
                matchings.append(word)

        for matching in matchings:
            print(matching)
