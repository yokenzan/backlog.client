# -*- coding: utf-8 -*-

class User:

    def __init__(self, id: int, userId: str, name: str, roleType: int):
        self.id       = id
        self.userId   = userId
        self.name     = name
        self.roleType = roleType

    def __str__(self):
        return self.name


