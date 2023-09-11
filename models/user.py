#!/usr/bin/python3

from models.base_model import BaseModel

class User(BaseModel):
    """creates user objects"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""