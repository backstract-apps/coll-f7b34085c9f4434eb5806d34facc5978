from pydantic import BaseModel,Field,field_validator

import datetime

import uuid

from typing import Any, Dict, List,Optional,Tuple

import re

class User1(BaseModel):
    id: int
    uaername: str
    name: str
    email: str
    password: str
    created_at: str


class ReadUser1(BaseModel):
    id: int
    uaername: str
    name: str
    email: str
    password: str
    created_at: str
    class Config:
        from_attributes = True


class User2(BaseModel):
    id: int
    created_at: str
    name: str
    username: str
    password: str
    email: str


class ReadUser2(BaseModel):
    id: int
    created_at: str
    name: str
    username: str
    password: str
    email: str
    class Config:
        from_attributes = True




class PostExternalApi(BaseModel):
    name: str = Field(..., max_length=100)
    address: str = Field(..., max_length=100)

    class Config:
        from_attributes = True



class PostTest(BaseModel):
    id: Any = Field(...)
    name: Any = Field(...)

    class Config:
        from_attributes = True

