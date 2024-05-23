from datetime import datetime as dt


class JournalEntry:
    default_datetime_format: str = '%Y-%m-%d %H:%M'
    
    def __init__(self, text: str):
        self.text = text
        # условно-защищённый атриубт — при доступе к нему из внешних отнсительно класса пространств имён для него будет активирован механизм подмены имён (name mangling)
        self.__datetime: dt = dt.now()
    
    # классический геттер — требуется вызывать как обычный метод
    def get_datetime(self) -> str:
        return f'{self.__datetime:{self.default_datetime_format}}'
    
    # классический сеттер
    def set_datetime(self, new_dt: str) -> None:
        self.__datetime = dt.strptime(new_dt, self.default_datetime_format)
    
    # свойство геттер — вызов осуществляется неявно, позволяя работать с атрибутом как бы не используя метод
    @property
    def datetime(self) -> str:
        return f'{self.__datetime:{self.default_datetime_format}}'
    
    # свойство сеттер
    @datetime.setter
    def datetime(self, new_dt: str) -> None:
        self.__datetime = dt.strptime(new_dt, self.default_datetime_format)


j1 = JournalEntry('первая запись')

# работа механизма подмены имён
# >>> j1.__dict__
# {'text': 'первая запись', '_JournalEntry__datetime': datetime.datetime(2024, 5, 22, 23, 6, 47, 156620)}


# >>> j1.datetime
# '2024-05-22 23:16'
# >>>
# >>> j1.datetime = '2024-05-22 23:55'
# >>>
# >>> j1.__dict__
# {'text': 'первая запись', '_JournalEntry__datetime': datetime.datetime(2024, 5, 22, 23, 55)}
# >>>
# >>> j1._JournalEntry__datetime
# datetime.datetime(2024, 5, 22, 23, 55)

