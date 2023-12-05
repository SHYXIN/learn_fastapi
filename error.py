class Missing(Exception):
    def __init__(self, msg: str):
        self.msg = msg


class Duplication(Exception):
    def __init__(self, msg: str):
        self.msg = msg
