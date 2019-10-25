# -*- coding: utf-8 -*-

class Priority:

    def __init__(self, id: int, name: str):
        self.id        = id
        self.name      = name

    def __str__(self):
        return 'Priority: ' + ', '.join([
            str(self.id),
            self.name,
        ])
