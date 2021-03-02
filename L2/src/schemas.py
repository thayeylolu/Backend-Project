from typing import List, Optional
from datetime import date
from pydantic import BaseModel

# base inherited by other Models (or schema as learnt on fastapi)


class UserBase(BaseModel):
    email: str
    username: str


class UserCreate(UserBase):
    password: str


class RentalBase(BaseModel):
    rental_date: date


class RentalCreate(RentalBase):
    due_date: date


class Rental(RentalBase):
    rid: int
    user_id: int
    movie_id: int

    class Config:
        orm_mode = True


class MovieBase (BaseModel):
    title: str
    description: str
    rating: int
    cost: int


class MovieCreate (MovieBase):
    replacement_cost: int
    past_return_charge: int


class Movie (MovieBase):
    mid: int
    is_rented: bool

    class Config:
        orm_mode = True


class User(UserBase):
    uid: int
    pass

    class Config:
        orm_mode = True
  
