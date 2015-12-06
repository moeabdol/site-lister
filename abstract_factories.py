import abc

class AbstractProtocolFactory(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, is_secure):
        self.is_secure = is_secure

    @abc.abstractmethod
    def create_protocol(self):
        raise NotImplementedError

    @abc.abstractmethod
    def create_port(self):
        raise NotImplementedError

    @abc.abstractmethod
    def create_parser(self):
        raise NotImplementedError

class AbstractPortFactory(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __str__(self):
        raise NotImplementedError

class AbstractParserFactory(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __call__(self, content):
        raise NotImplementedError
