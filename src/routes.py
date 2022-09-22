from src import app
from .resources.users import Users


@app.route("/")
def hello():
    return "Hello"


@app.route("/users", methods=["GET"])
def get_all_users():
    return Users.get()


@app.route("/users", methods=["POST"])
def create_new_users():
    return Users.post()


@app.route("/users/<int:idx>", methods=["PUT"])
def update_user(idx):
    return Users.put(idx)


@app.route("/users/<int:idx>", methods=["PATCH"])
def modificate_user(idx):
    return Users.patch(idx)


@app.route("/users/<int:idx>", methods=["DELETE"])
def delete_user(idx):
    return Users.delete(idx)
