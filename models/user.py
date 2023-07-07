#!/usr/bin/python3
"""Module with User class that inherits from BaseModel"""

from models.base_model import BaseModel


class User(BaseModel):
    """Class that describes the user"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
