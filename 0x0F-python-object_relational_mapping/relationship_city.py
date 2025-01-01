#!/usr/bin/python3
from sqlalchemy import Column, Integer, String, text, ForeignKey
from relationship_state import Base
"""
    Contains the class definition of a City.
"""


class City(Base):
    """
        The ``City`` class.
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
