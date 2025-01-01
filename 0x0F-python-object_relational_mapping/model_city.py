#!/usr/bin/python3
"""Contains the class definition of a City"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base, State

class City(Base):
    """City class representing cities in a database."""
    __tablename__ = 'cities'
    
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    # Adding a relationship for easier access to related state
    state = relationship("State", back_populates="cities")

# Ensure State model is updated to reflect back relationship
# In model_state.py:
# class State(Base):
#     __tablename__ = 'states'
#     ...
#     cities = relationship("City", back_populates="state")
