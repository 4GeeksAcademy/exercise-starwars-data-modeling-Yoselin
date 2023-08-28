import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    

class People(Base):
    __tablename__ = 'people'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    height = Column(Integer)
    mass = Column(Integer)
    hair_color = Column(String(250))
    skin_color = Column(String(250))
    eye_color = Column(String(250))
    birth_year = Column(Integer)
    gender = Column(String(250))
    # person_id = Column(Integer, ForeignKey('person.id'))
    # person = relationship(Person)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    rotation_period = Column(String(250))
    orbital_period = Column(String(250))
    diameter = Column(Integer)
    climate = Column(String(250))
    gravity = Column(Integer)
    terrain = Column(String(250))
    surface_water = Column(Integer)
    population = Column(Integer)
    residents = Column(String(250))

class Starships(Base):
    __tablename__ = 'starships'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    model = Column(String(250))
    manufacturer = Column(String(250))
    cost_in_credits = Column(Integer)
    length = Column(Integer)
    max_atmosphering_speed = Column(Integer)
    crew = Column(Integer)
    passengers = Column(String(250))
    cargo_capacity = Column(Integer)
    consumables = Column(String(250))
    hyperdrive_rating = Column(Integer)
    mglt = Column(Integer)
    starship_class = Column(String(250))
    pilots = Column(String(250))

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    cargo_capacity = Column(Integer)
    consumables = Column(String(250))
    cost_in_credits = Column(Integer)
    created = Column(Integer)
    crew = Column(Integer)
    edited = Column(Integer)
    length = Column(Integer)
    manufacturer = Column(String(250))
    max_atmosphering_speed = Column(Integer)
    model = Column(String(250))
    passenger = Column(String(250))
    pilots = Column(String(250))

class Favorite (Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    people_id = Column(Integer, ForeignKey('people.id'))
    planets_id = Column(Integer, ForeignKey('planets.id'))
    starships_id = Column(Integer, ForeignKey('starships.id'))
    vehicles_id = Column(Integer, ForeignKey('vehicles.id'))
    usuario = relationship("Usuario")
    people = relationship("People")
    planets = relationship("Planets")
    starships = relationship("Starships")    
    vehicles = relationship("Vehicles")    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
