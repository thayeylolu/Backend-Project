from sqlalchemy.orm import Session
from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.uid == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

# movie


def get_movie(db: Session, movie_id: int):
    return db.query(models.Movie).filter(models.Movie.mid == movie_id).first()


def get_movie_by_title(db: Session, title: str):
    return db.query(models.Movie).filter(models.Movie.title == title).first()


def get_movies(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Movie).offset(skip).limit(limit).all()

# get rental


def get_rental(db: Session, rental_id: int):
    return db.query(models.Rental).filter(models.Rental.rid == rental_id).first()


def get_rentals(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Rental).offset(skip).limit(limit).all()

# create user


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(username=user.username,
                          email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# create movie


def create_movie(db: Session, movie: schemas.MovieCreate):
    db_movie = models.Movie(
        **movie.dict()
    )
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie

# create rental


def create_rental(db: Session, rental: schemas.RentalCreate, user_id: int, movie_id: int):
    db_rental = models.Rental(
        **rental.dict(), user_id=user_id, movie_id=movie_id)
    db.add(db_rental)
    db.commit()
    db.refresh(db_rental)
    return db_rental

# delete by id:


def delete_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.uid == user_id).delete(synchronize_session=False)

def delete_rental_by_id(db: Session, rental_id: int):
    return db.query(models.Rental).filter(models.Rental.rid == rental_id).delete(synchronize_session=False)


def delete_movie_by_id(db: Session,  movie_id: int):
    return db.query(models.Movie).filter(models.Movie.mid == movie_id).delete(synchronize_session=False)

# delete by email, title


def delete_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email==email).delete(synchronize_session=False)


def delete_movie_by_title(db: Session, title: str):
    return db.query(models.Movie).filter(models.Movie.title == title).delete(synchronize_session = False)

