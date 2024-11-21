from data.data import Data


class TableRow(Data):

    key: int
    content: str

    def get_key(self) -> int:
        return self.key

    def __init__(self, key: int, content: str = ""):
        self.key = key
        self.content = content

    def __gt__(self, other: 'TableRow'):
        return self.key > other.key

    def __eq__(self, other: 'TableRow'):
        return self.key == other.key

    def __ne__(self, other: 'TableRow'):
        return self.key != other.key

    def __repr__(self):
        return f"<{self.key}:{self.content}>"
    