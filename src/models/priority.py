# -*- coding: utf-8 -*-

class Priority:
    """
        優先度
    """

    def __init__(self, id: int, name: str):
        self.id        = id
        self.name      = name

    def __str__(self):
        return ', '.join([
            str(self.id),
            self.name,
        ])

    def to_list_item(self) -> str:
        return f'{str(self.id)} # {self.name}'
