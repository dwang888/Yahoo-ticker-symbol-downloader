from ..SymbolDownloader import SymbolDownloader
from ..symbols.Warrant import Warrant

from ..compat import unicode

class WarrantDownloader(SymbolDownloader):
    def __init__(self):
        SymbolDownloader.__init__(self, "Warrant")

    def decodeSymbolsContainer(self, symbolsContainer):
        symbols = []
        for row in symbolsContainer:
            ticker = unicode(row.contents[0].string)
            name = row.contents[1].string
            if name is not None:
                name = unicode(name)
            type = row.contents[3].string
            categoryName = row.contents[4].string
            if categoryName is not None:
                categoryName = unicode(categoryName)
            categoryNr = 0
            if(categoryName != None):
                categoryNr = int(row.contents[4].a.get('href').split("/").pop().split(".")[0])
            exchange = row.contents[5].string
            if exchange is not None:
                exchange = unicode(exchange)

            symbols.append(Warrant(ticker, name, exchange, categoryName, categoryNr))
        return symbols

    def getRowHeader(self):
        return SymbolDownloader.getRowHeader(self) + ["categoryName", "categoryNr"]
