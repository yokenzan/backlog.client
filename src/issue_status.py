# -*- coding: utf-8 -*-

class IssueStatus:

    def __init__(self, id: int, name: str, color: str, order: int):
        self.id        = id
        self.name      = name
        self.color     = color
        self.order     = order

    def __str__(self):
        return self.name
