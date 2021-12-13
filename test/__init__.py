class WithPositional:
    """A class"""

    def __init__(self, a, /) -> None:
        self.a = a  #: A property

class WithoutPositional:
    """A class"""

    def __init__(self, a) -> None:
        self.a = a  #: A property
