#!/usr/bin/python3
"""This module defines the user module"""
from models.base_model import BaseModel

class User(BaseModel):
    """Defines class User which inherits BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
