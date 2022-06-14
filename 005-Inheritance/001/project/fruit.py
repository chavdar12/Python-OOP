from food import Food


class Fruit(Food):
    def __init__(self, name, expiration_date):
        self.name = name
        super(Fruit, self).__init__(expiration_date)
