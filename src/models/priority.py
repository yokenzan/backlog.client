# -*- coding: utf-8 -*-


class Priority:
    """
    Priority of Backlog issue.
    """

    def __init__(self, priority_id: int, name: str):
        self.priority_id = priority_id
        self.name        = name

    def __str__(self):
        return ", ".join([str(self.priority_id), self.name, ])

    def to_list_item(self) -> str:
        return f"{str(self.priority_id)} # {self.name}"
