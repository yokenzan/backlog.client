# -*- coding: utf-8 -*-


class IssueType:
    """
    Type of Backlog issue.
    """

    def __init__(self, id: int, name: str, color: str, order: int):
        self.id = id
        self.name = name
        self.color = color
        self.order = order

    def __str__(self):
        return self.name

    def to_list_item(self) -> str:
        return f"{str(self.id)} # {self.name} {self.color}"
