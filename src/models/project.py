# -*- coding: utf-8 -*-

class Project:

    def __init__(self, id: int, projectKey: str, name: str):
        self.id         = id
        self.projectKey = projectKey
        self.name       = name

    def __str__(self):
        return 'Project: ' + ', '.join([
            str(self.id),
            self.projectKey,
            self.name,
        ])

