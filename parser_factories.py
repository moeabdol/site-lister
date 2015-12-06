from BeautifulSoup import BeautifulStoneSoup
from abstract_factories import AbstractParserFactory

class HTTPParser(AbstractParserFactory):
    def __call__(self, content):
        filenames = []
        soup = BeautifulStoneSoup(content)
        links = soup.table.findAll("a")
        for link in links:
            filenames.append(link.text)
        return "\n".join(filenames)

class FTPParser(AbstractParserFactory):
    def __call__(self, content):
        lines = content.split("\n")
        filenames = []
        for line in lines:
            splitted_line = line.split(None, 8)
            if len(splitted_line) == 9:
                filenames.append(splitted_line[-1])
        return "\n".join(filenames)
