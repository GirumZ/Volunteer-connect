#!/usr/bin/python3
""" User model"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import mapper
import mysql.connector
import uuid
from datetime import datetime
import models


class User(Base, BaseModel):
    """ User class definition"""

    __tablename__ = 'users'
    
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)