class Request:
    """
    Request access to disk
    """

    def __init__(self, block: int):
        self.__block = block

    @property
    def block(self) -> int:
        return self.__block

    @block.setter
    def block(self, new_block: int):
        self.__block = new_block

    def __repr__(self) -> str:
        return str(self.__block)
