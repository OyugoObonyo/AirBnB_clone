#!/usr/bin/python3
"""
inherit from BaseModel
"""
from models.base_model import BaseModel

class City(BaseModel):
    """class user that inheirts from Base model"""
    state_id = ""
    name= ""
