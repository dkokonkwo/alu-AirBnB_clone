#!/usr/bin/python3
"""it defines review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """public class attributes"""
    place_id = ""
    user_id = ""
    text_id = ""
