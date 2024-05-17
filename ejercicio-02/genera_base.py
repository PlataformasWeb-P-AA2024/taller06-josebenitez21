

from sqlalchemy import create_engine

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine('sqlite:///basepaises.db')

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


from sqlalchemy import Column, Integer, String

class Paises(Base):
    __tablename__ = 'paises'
    
    nombrePais = Column(String, primary_key=True, nullable=True)
    capital = Column(String, nullable=True)
    continente = Column(String, nullable=True)
    dial = Column(String, nullable=True)
    geoname_id = Column(String, nullable=True)
    itu = Column(String, nullable=True)
    lenguajes = Column(String, nullable=True)
    tipoEstado = Column(String, nullable=True)
    
    


Base.metadata.create_all(engine)

