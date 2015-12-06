from abstract_factories import AbstractPortFactory

class HTTPSecurePort(AbstractPortFactory):
    def __str__(self):
        return "443"

class HTTPPort(AbstractPortFactory):
    def __str__(self):
        return "80"

class FTPPort(AbstractPortFactory):
    def __str__(self):
        return "21"
