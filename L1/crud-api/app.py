from fastapi import FastAPI
import json
import uvicorn
from models.model import Rentals, Users, Movies
# Init
app = FastAPI()


# read the files:
with open("data/movies.json") as movies_content:
    moviesContent = json.load(movies_content)

with open("data/users.json") as users_content:
    usersContent = json.load(users_content)

with open("data/rentals.json") as rentals_content:
    rentalsContent = json.load(rentals_content)


# 1. GET ALL - READ
@app.get('/movies')
async def allMovies():
    return [movie for movie in moviesContent]


@app.get('/users')
async def allUsers():
    return [user for user in usersContent]


@app.get('/rentals')
async def allRentals():
    return [rental for rental in rentalsContent]

# 2  CREATE


def write_json(filename, value, req_body):
    with open(filename) as json_file:
        data = json.load(json_file)
        temp = data[str(value)]
        # appending data to emp_details
        temp.append(req_body.dict())

    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


@app.post('/addRentals')
async def create_rental(rental: Rentals):
    write_json('data/rentals.json', 'rentals', rental)
    return rental.dict()


@app.post('/addMovies')
async def create_movies(movie: Movies):
    write_json('data/movies.json', 'movies', movie)
    return movie.dict()


@app.post('/addUsers')
async def create_users(user: Users):
    write_json('data/users.json', 'users', user)
    return user.dict()

# 3. PUT


def update_json(filename, value, req_body, check_id):
    with open(filename) as json_file:
        data = json.load(json_file)
        temp = data[str(value)]
        for item in temp:
            if item['userId'] == check_id:
                item = req_body.dict()
                temp.append(item)
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


@app.put('/updateRentals/{rentalid}')
async def update_rental(rentalid: int, rental: Rentals):
    update_json('data/rentals.json', 'rentals', rental, rentalid)
    return (rental.dict())


@app.put('/updateMovies/{movieid}')
async def update_movies(movieid: int, movie: Movies):
    update_json('data/movies.json', 'movies', movie, movieid)
    return (movie.dict())


@app.put('/addUsers/{userid}', response_model=Users)
async def update_user(userid: int, user: Users):
    update_json('data/users.json', 'users', user, userid)
    return (user.dict())


# 4 Get a dict


def get_object(filename, value, check_id):
    with open(filename) as json_file:
        data = json.load(json_file)
        temp = data[str(value)]
        for item in temp:
            if item['userId'] == check_id:
                return(item)


@app.get("/users/{userid}", response_model=Users)
async def read_user(userid: str):
    return get_object([item_id])
