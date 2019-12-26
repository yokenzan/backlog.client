# -*- coding: utf-8 -*-

class Project:
    """
        プロジェクト
    """

    def __init__(self, id: int, key: str, name: str):
        self.id   = id
        self.key  = key
        self.name = name

    def __str__(self):
        return 'Project: ' + ', '.join([
            str(self.id),
            self.key,
            self.name,
        ])

