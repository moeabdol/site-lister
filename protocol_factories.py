from abstract_factories import AbstractProtocolFactory
from port_factories import HTTPSecurePort, HTTPPort, FTPPort
from parser_factories import HTTPParser, FTPParser

class HTTPFactory(AbstractProtocolFactory):
    def create_protocol(self):
        if self.is_secure:
            return "https"
        return "http"

    def create_port(self):
        if self.is_secure:
            return HTTPSecurePort()
        return HTTPPort()

    def create_parser(self):
        return HTTPParser()

class FTPFactory(AbstractProtocolFactory):
    def create_protocol(self):
        return "ftp"

    def create_port(self):
        return FTPPort()

    def create_parser(self):
        return FTPParser()
