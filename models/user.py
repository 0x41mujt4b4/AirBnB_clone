#!/usr/bin/python3
"""
user module inherits from BaseModel
"""
from .base_model import BaseModel


class User(BaseModel):
    """
    User class inherits from BaseModel
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
