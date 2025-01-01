#!/usr/bin/python3
"""
Defines the City class, representing a city in the database.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """
    Represents a city and its attributes.

    Attributes:
        id (int): Unique identifier for the city.
        name (str): Name of the city.
        state_id (int): Identifier for the associated state.
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
