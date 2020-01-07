# -*- coding: utf-8 -*-

class User:
    """
    Backlog user.
    """

    def __init__(self, user_id: int, user_key: str, name: str, roleType: int):
        self.user_id  = user_id
        self.user_key = user_key
        self.name     = name
        self.roleType = roleType

    def __str__(self):
        return self.name

    def to_list_item(self) -> str:
        return f'{str(self.user_id)} # {self.name}'
