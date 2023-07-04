class Persona:
    def __init__(self, id, name, date) -> None:
        self.id = id
        self.name = name
        self.date = date
    def __repr__(self) -> str:
        return f'{self.name} - {self.date} \n'