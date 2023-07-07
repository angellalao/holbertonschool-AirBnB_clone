#!/usr/bin/python3
"""Module with Review class that inherits from BaseModel"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Class that describes the user"""
    place_id = ""
    user_id = ""
    text = ""
