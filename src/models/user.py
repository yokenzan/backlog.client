# -*- coding: utf-8 -*-

class User:
    """
    Backlog user.
    """

    def __init__(self, user_id: int, userId: str, name: str, roleType: int):
        self.user_id  = user_id
        self.userId   = userId
        self.name     = name
        self.roleType = roleType

    def __str__(self):
        return self.name

    def to_list_item(self) -> str:
        return f'{str(self.user_id)} # {self.name}'

