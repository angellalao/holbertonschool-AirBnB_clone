#!/usr/bin/python3
"""Module with City class that inherits from BaseModel"""

from models.base_model import BaseModel


class City(BaseModel):
    """Class that describes the city"""
    state_id = ""
    name = ""
