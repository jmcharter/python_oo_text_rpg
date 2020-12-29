class Item():
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return f"Item Object \n{self.name} \n{self.description} \
            \nValue: {self.value}"


class Weapon(Item):
    def __init__(self, name, description, value, attack_value):
        super().__init__(name, description, value)
        self.attack_value = attack_value
