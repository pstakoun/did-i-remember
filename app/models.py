from sqlalchemy import Column, Integer, String
from app.database import Base

class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    occurrences = Column(Integer)

    def __init__(self, name):
        self.name = name
        self.occurrences = 1

    def __repr__(self):
        return '<Item '+str(self.id)+' '+self.name+' '+str(self.occurrences)+'>'

class ItemConnection(Base):
    __tablename__ = 'itemconnections'
    id1 = Column(Integer, primary_key=True)
    id2 = Column(Integer)
    occurrences = Column(Integer)

    def __init__(self, id1, id2):
        self.id1 = id1
        self.id2 = id2

    def __repr__(self):
        return '<ItemConnection '+str(self.id1)+' '+str(self.id2)+' '+str(self.occurrences)+'>'
