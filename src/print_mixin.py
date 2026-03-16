class PrintMixin:
    def __init__(self, *args, **kwargs) -> None:
        print(repr(self))
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return (f"{self.__class__.__name__}('{self.name}',"
                f" '{self.description}', '{self.price}', {self.quantity})")
