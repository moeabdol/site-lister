from protocol_factories import HTTPFactory, FTPFactory
from connector import Connector
import urllib2

domain = "ftp.freebsd.org"
path   = "/pub/FreeBSD/"

protocol = input(
    "Connecting to {}. Which Protocol to use? (0-http, 1-ftp): ".format(domain))

if protocol == 0:
    is_secure = bool(input("Use secure connection? (1-yes, 0-no): "))
    factory = HTTPFactory(is_secure)
else:
    factory = FTPFactory(False)

connector = Connector(factory)
try:
    content = connector.read(domain, path)
except urllib2.URLError, e:
    print "Can not access resource with this method"
else:
    print connector.parse(content)
