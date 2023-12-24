from datetime import datetime
from abc import abstractmethod
from pathlib import Path
from typing import Dict, Iterable, List
from alarm.Alarm import Alarm


class AbstractStorage(object):
    """ Определяет интерфейс хранилища будильников. """

    @abstractmethod
    def get_all(self) -> Iterable[Alarm]:
        """ Возвращает набор всех будильников из хранилища. """
        raise NotImplementedError

    @abstractmethod
    def put_all(self, alarm: Alarm):
        """ Складывает будильники в хранилище. """
        raise NotImplementedError


class FileStorage(AbstractStorage):
    """ Реализация хранилища в файле. """

    def __init__(self, path: Path, delimiter: str = ';;'):
        self.__path = path
        self.__delimiter = delimiter

        # NOTE: Если файла хранилища нет по указанному пути, создадим его.
        if not self.__path.exists():
            self.__path.touch()

    def get_all(self) -> Dict[int, Alarm]:
        # NOTE: Открываем файл хранилища на чтение.
        dictionary: Dict[int, Alarm] = {}
        with self.__path.open('r') as my_file:
            # NOTE: Читаем файл построчно и для каждой строки формируем будильник.
            for line in my_file:
                alarm: Alarm = self.__make_alarm(line.removesuffix('\n'))
                dictionary[alarm.alarm_id] = alarm

        return dictionary

    def set_all(self, alarms: Iterable[Alarm]):
        lines = [self.__make_line(a) for a in alarms]
        self.__path.write_text('\n'.join(lines))

    def __str_from_time(self, dtime: datetime) -> str:
        result = str(dtime.month) + '/' + str(dtime.day) + '/' + str(dtime.year % 100) + ' ' + str(dtime.hour) + ':' + str(dtime.minute) + ':' + str(dtime.second)
        return result

    def __make_line(self, alarm: Alarm) -> str:
        fields: List[str] = [str(alarm.alarm_id), alarm.name, str(alarm.is_on), self.__str_from_time(alarm.time)]
        return f'{self.__delimiter.join(fields)}'

    def __str_to_bool(self, str_bool: str) -> bool:
        if str_bool == 'True':
            return True
        else:
            return False

    def __make_alarm(self, line: str) -> Alarm:
        try:
            data = line.split(self.__delimiter)
            alarm_id, name, is_on, time = data
            al_time = datetime.strptime(time, '%m/%d/%y %H:%M:%S')
            alarm = Alarm(name, al_time)
            alarm.alarm_id = int(alarm_id)
            alarm.is_on = self.__str_to_bool(is_on)
            return alarm
        except Exception as ex:
            print(ex)
