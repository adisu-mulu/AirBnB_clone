#!/usr/bin/python3
"""This module defines the review """
from models.base_model import BaseModel


class Review(BaseModel):
    """This class defines the review and inherits BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
