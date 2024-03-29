from dataclasses import dataclass
from datetime import datetime


@dataclass
class Word:
    word: str
    meaning: str
    added_date: float
    recapped_date: float = 0.0
    recap_count: int = 0

    def __str__(self) -> str:
        return f"- {self.word}: {self.meaning}"

    def get_added_date(self) -> datetime:
        return datetime.fromtimestamp(self.added_date)

    def get_recapped_date(self) -> datetime:
        return datetime.fromtimestamp(self.recapped_date)
