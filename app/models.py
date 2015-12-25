from sqlalchemy import Column, Integer, String
from app.database import Base

class Item(Base):
    __tablename__ = 'items'
    name = Column(String(64), primary_key=True)
    occurrences = Column(Integer)

    def __init__(self, name):
        self.name = name
        self.occurrences = 1

    def __repr__(self):
        return '<Item '+str(self.id)+' '+self.name+' '+str(self.occurrences)+'>'

class ItemConnection(Base):
    __tablename__ = 'itemconnections'
    item1 = Column(String(64), primary_key=True)
    item2 = Column(String(64))
    occurrences = Column(Integer)

    def __init__(self, id1, id2):
        self.item1 = item1
        self.item2 = item2
        self.occurrences = 1

    def __repr__(self):
        return '<ItemConnection '+str(self.item1)+' '+str(self.item2)+' '+str(self.occurrences)+'>'
