from sqlalchemy import Column, Integer, String
from app.database import Base

class Item(Base):
    __tablename__ = 'items'
    name = Column(String(64), primary_key=True)
    occurrences = Column(Integer)

    def __init__(self, name):
        self.name = name
        self.occurrences = 0

    def __repr__(self):
        return '<Item:'+self.name+'x'+str(self.occurrences)+'>'

class ItemConnection(Base):
    __tablename__ = 'itemconnections'
    id = Column(Integer, primary_key=True)
    item1 = Column(String(64))
    item2 = Column(String(64))
    occurrences = Column(Integer)

    def __init__(self, item1, item2):
        self.item1 = item1
        self.item2 = item2
        self.occurrences = 0

    def __repr__(self):
        return '<ItemConnection:'+self.item1+'<->'+self.item2+'x'+str(self.occurrences)+'>'

class ItemSpelling(Base):
    __tablename__ = 'itemspellings'
    id = Column(Integer, primary_key=True)
    item = Column(String(64))
    spelling = Column(String(64))
    occurrences = Column(Integer)

    def __init__(self, item, spelling):
        self.item = item
        self.spelling = spelling
        self.occurrences = 0

    def __repr__(self):
        return '<ItemSpelling:'+self.item+'<->"'+self.spelling+'"x'+str(self.occurrences)+'>'
