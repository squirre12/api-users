from src import api
from .resources.users import Users

api.add_resource(Users, '/users', '/users/<id>', strict_slashes=False)
