#!/usr/bin/python3
"""
Module that contains the State class definition
and instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """
    Class that defines each state
    Attributes:
        id: state id
        name: state name
        cities: relationship with City class
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                         cascade="all, delete-orphan")
