from action import Action


class QuitAction(Action):
    name = "프로그램 종료"

    def __init__(self, quit_function):
        super().__init__()

        self.quit = quit_function

    def tick(self):
        self.quit()
