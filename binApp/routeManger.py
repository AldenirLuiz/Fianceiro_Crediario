from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class RouteData(Base):
    __tablename__ = "route_data"
    id = Column(Integer, primary_key=True)
    city = Column(String)
    name = Column(String)
    address = Column(Integer)
    # ... Adicione outros campos aqui ...

engine = create_engine("sqlite:///route_data.db")
Session = sessionmaker(bind=engine)

def add_route_data(city, route_number):
    session = Session()
    new_table_name = f"{city}_route_{route_number}"
    RouteData.__table__.name = new_table_name
    RouteData.__table__.create(bind=engine, checkfirst=True)
    # Adicione os dados da rota aqui, usando a sessão do SQLAlchemy ...
    session.commit()
    session.close()

# Adicione uma nova rota ao banco de dados
add_route_data("City A", 1)