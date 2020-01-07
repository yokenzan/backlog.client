# -*- coding: utf-8 -*-


class Project:
    """
    Backlog project.
    """

    def __init__(self, project_id: int, key: str, name: str):
        self.project_id = project_id
        self.key        = key
        self.name       = name

    def __str__(self):
        return "Project: " + \
            ", ".join([str(self.project_id), self.key, self.name, ])
