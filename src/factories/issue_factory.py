# -*- coding: utf-8 -*-

from src.models    import Issue
from src.factories import UserFactory, IssueStatusFactory, IssueTypeFactory, PriorityFactory

class IssueFactory:

    def __init__(
            self,
            userFactory:        UserFactory,
            issueTypeFactory:   IssueTypeFactory,
            issueStatusFactory: IssueStatusFactory,
            priorityFactory:    PriorityFactory
    ):
        self.userFactory        = userFactory
        self.issueStatusFactory = issueStatusFactory
        self.issueTypeFactory   = issueTypeFactory
        self.priorityFactory    = priorityFactory

    def generate(self, row: dict) -> Issue:
        return Issue(
            row['id'],
            row['issueKey'],
            row['keyId'],
            self.issueTypeFactory.generate(row['issueType']),
            row['summary'],
            row['description'],
            self.userFactory.generate(row['assignee']),
            self.priorityFactory.generate(row['priority']),
            self.issueStatusFactory.generate(row['status'])
        )

