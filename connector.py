import abc
import urllib2

class Connector(object):
    def __init__(self, factory):
        self.protocol = factory.create_protocol()
        self.port     = factory.create_port()
        self.parser   = factory.create_parser()

    def read(self, host, path):
        url = self.protocol + "://" + host + ":" + str(self.port) + path
        print "Connecting to", url
        return urllib2.urlopen(url, timeout=2).read()

    def parse(self, content):
        return self.parser(content)
