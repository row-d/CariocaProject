class CardInterface:
    def __init__(self, id: str, number: int, pinta: str):
        pass

    @property
    def id(self):
        raise NotImplementedError("id property not implemented")

    @property
    def number(self):
        raise NotImplementedError("number property not implemented")

    @number.setter
    def number(self, value):
        raise NotImplementedError("number property not implemented")

    @property
    def pinta(self):
        raise NotImplementedError("pinta property not implemented")

    @pinta.setter
    def pinta(self, value):
        raise NotImplementedError("pinta property not implemented")
