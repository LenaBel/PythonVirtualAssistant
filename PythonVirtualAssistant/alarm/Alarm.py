from dataclasses import dataclass
from datetime import datetime


@dataclass
class Alarm:
    alarm_id: int
    name: str
    is_on: bool = True
    time: datetime = datetime.now()

    def __init__(self, name: str, time: datetime):
        self.name = name
        self.time = time

