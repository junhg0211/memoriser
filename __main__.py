from database import Database

from action import QuitAction, WordAppendAction, RecapAction


class Frame:
    def __init__(self):
        self.running = True

        self.database = Database("database.json")

        self.actions = list()
        self.actions.append(QuitAction(self.quit))
        self.actions.append(WordAppendAction(self.database))
        self.actions.append(RecapAction(self.database))

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
