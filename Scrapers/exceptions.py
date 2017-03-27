
class MissingAttributeException(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


class MissingPriceException(MissingAttributeException):
    def __init__(self, *args, **kwargs):
        MissingAttributeException.__init__(self, *args, **kwargs)