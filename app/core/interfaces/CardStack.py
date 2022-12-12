class CardStackInterface:
    def __init__(self) -> None:
        pass

    @property
    def cards(self):
        raise NotImplementedError("cards property not implemented")

    @cards.setter
    def cards(self, value):
        raise NotImplementedError("cards property not implemented")

    @classmethod
    def shuffle(self):
        raise NotImplementedError("shuffle method not implemented")

    @classmethod
    def takeCard(self):
        raise NotImplementedError("takeCard method not implemented")

    @classmethod
    def addCard(self):
        raise NotImplementedError("addCard method not implemented")
