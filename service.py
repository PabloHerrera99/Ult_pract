from base import Base
from fecha import Fecha
from persona import Persona

class Service:
    def __init__(self) -> None:
        self.base = []
    
    def add(self, persona, base):
        base.data[persona.id] = persona

    def order_by_fecha(self, base):
        list = []
        for i in (base.data.values()):
            list.append(i)
        for i in range(len(list)-1):
            for j in range(i+1, len(list)):
                if list[i].date.compare_to(list[j].date) == 1:
                    list[i], list[j] = list[j],list[i]

        return list
    
    def order_by_apellido(self, base):
        list = []
        for i in (base.data.values()):
            list.append(i)
        for i in range(len(list)-1):
            for j in range(i+1, len(list)):
                if list[i].name > list[j].name:
                    list[i], list[j] = list[j],list[i]
        return list

if __name__ == '__main__':
    fecha1 = Fecha(2022, 3, 14)
    fecha2 = Fecha(2024, 6, 1)
    persona1 = Persona(5, 'Perez', fecha1)
    persona2 = Persona(2, 'Gomez', fecha2)
    base = Base()
    service = Service()
    service.add(persona1, base)
    service.add(persona2, base)
    print(base.data.values())
    print(persona1)
    b = base.data[persona1.id]
    print(b.date.day)
    a = service.order_by_fecha(base)
    print(a)