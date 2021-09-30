class Failure:
    def __init__(self, exception: Exception):
        self.error = exception

    def throw(self, *args):
        self.error.args = args
        raise self.error
        