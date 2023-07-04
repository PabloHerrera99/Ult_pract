import datetime

class Fecha:
    def __init__(self, year = 2023, month = 1, day = 1) -> None:
        self.year = year
        self.month = month
        self.day = day
    
    def __repr__(self) -> str:
        return f'{self.day} / {self.month} / {self.year}'
    
    def compare_to(self, fecha2):
        fecha_1 = datetime.datetime(self.year, self.month, self.day)
        fecha_2 = datetime.datetime(fecha2.year, fecha2.month, fecha2.day)
    
        if fecha_1 < fecha_2:
            return -1
        if fecha_1 > fecha_2:
            return 1
        if fecha_1 == fecha_2:
            return 0
            