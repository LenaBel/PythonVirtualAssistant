from dataclasses import dataclass
from datetime import datetime


@dataclass
class Alarm:
    alarm_id: int
    name: str
    is_on: bool = False
    time: datetime = None

