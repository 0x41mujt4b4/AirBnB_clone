#!/usr/bin/python3
"""
review module inherits from BaseModel
"""
from .base_model import BaseModel


class Review(BaseModel):
    """
    Review class inherits from BaseModel
    """
    place_id = ""
    user_id = ""
    text = ""
