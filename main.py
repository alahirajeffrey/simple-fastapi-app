from fastapi import FastAPI

# instatiate app
app = FastAPI()

# fake database
fake_db = [
    {'id': 1, 'name': 'jeffrey'},
    {'id': 2, 'name': 'alahira'},
    {'id': 3, 'name': 'calvin'}
]

# root route


@app.get('/')
async def root():
    return ("Simple fastapi app")

# get all users


@app.get('/users')
def get_all_users():
    return (fake_db)

# get single user


@app.get("/users/{id}")
def get_single_user(id: int):
    for user in fake_db:
        if(int(user['id'])) == id:
            return (user)

# delete single user


@app.delete("/users/{id}")
def delete_single_user(id: int):
    for user in fake_db:
        if(int(user['id'])) == int(id):
            fake_db.remove(user)
            return (fake_db)

# create user


@app.post("/users")
def create_user(user: dict):
    fake_db.append(user)
    return (fake_db)

# update user


@app.put('/users{id}')
def update_user(id: int, body: dict):
    for user in fake_db:
        if(int(user['id'])) == id:
            user['name'] = body['name']
            return (fake_db)
