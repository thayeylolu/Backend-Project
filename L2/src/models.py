from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    uid = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    username = Column(String)

    # relationship
    rentals = relationship("Rental", back_populates="lender")


class Rental (Base):
    __tablename__ = "rentals"

    rid = Column(Integer, primary_key=True, index=True)
    rental_date = Column(Date)
    return_date = Column(Date)
    due_date = Column(Date)
    user_id = Column(Integer, ForeignKey("users.uid"))  # foreign key
    movie_id = Column(Integer, ForeignKey("movies.mid"))  # foreign key

    # relationship
    lender = relationship("User", back_populates="rentals")
    movie = relationship("Movie", back_populates="rental_shelf")


class Movie (Base):
    __tablename__ = "movies"

    mid = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    rating = Column(Integer)
    cost = Column(Integer)
    replacement_cost = Column(Integer)
    past_return_charge = Column(Integer)
    is_rented = Column(Boolean, default=False)

    # relationship
    rental_shelf = relationship("Rental", back_populates="movie")
