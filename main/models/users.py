#!/usr/bin/python3
""" User Module """
from models.baseModel import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
import models


class User(BaseModel, Base):
    """This class defines a user by various attributes according
    to selected storage"""

    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    photographer_id = Column(Integer, ForeignKey('photographer.id'))
    client_id = Column(Integer, ForeignKey('client.id'))
    photographer = relationship("Photographer", back_populates="user")
    client = relationship("Client", back_populates="user")


    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)



class Photographer(BaseModel, Base):
    """Model for Photographers"""

    __tablename__ = 'photographers'

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    # Add specific photographer attributes here

    def __init__(self, *args, **kwargs):
        """initializes photographer"""
        super().__init__(*args, **kwargs)


class Client(BaseModel, Base):
    """Model for Clients"""

    __tablename__ = 'clients'

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    # Add specific client attributes here

    def __init__(self, *args, **kwargs):
        """initializes client"""
        super().__init__(*args, **kwargs)
