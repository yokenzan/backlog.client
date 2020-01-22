# -*- coding: utf-8 -*-


from typing       import List
from src.api      import AbstractClient
from src.usecases import GetUsers, GetPriorities, GetIssueTypes, GetIssueStatuses


class AddIssue:

    def __init__(
        self,
        get_users:          GetUsers,
        get_priorities:     GetPriorities,
        get_issue_types:    GetIssueTypes,
        get_issue_statuses: GetIssueStatuses
    ):
        self.usecases = [
            get_users, get_priorities, get_issue_types, get_issue_statuses,
        ]

    def handle(self):
        for usecase in self.usecases:
            [print(i.to_list_item()) for i in usecase.handle()]
            print('-' * 50)
