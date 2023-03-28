from abc import ABC


class Armor(ABC):
    def __init__(self, name, defence):
        self.name = name
        self.defence = defence


class Cloack(Armor):
    def __init__(self, name, defence=10, skill="Cloack"):
        self.name = name
        self.defence = defence
        self.skill = skill


class Helmet(Armor):
    def __init__(self, name, defence=5, skill="Helmet"):
        self.name = name
        self.defence = defence
        self.skill = skill
