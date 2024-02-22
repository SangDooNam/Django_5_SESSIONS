"""Data for the common views"""
from config.store import CustomStore
from django.contrib.auth.hashers import make_password


class UserStore(CustomStore):
    """Store for the users."""

    model_name = "users"
    backup = [
        {
            "name": "admin",
            "password": make_password("admin"),
            "role": "admin"
        },
        {
            "name": "james",
            "password": make_password("hendrix"),
            "role": "editor"
        },
        {
            "name": "fred",
            "password": make_password("baggins"),
            "role": "user"
        },
        {
            "name": "ganesh",
            "password": make_password("the_grey"),
            "role": "user"
        }
    ]
