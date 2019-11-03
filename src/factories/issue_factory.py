# -*- coding: utf-8 -*-

from src.issue                          import *
from src.factories.user_factory         import *
from src.factories.issue_type_factory   import *
from src.factories.issue_status_factory import *
from src.factories.priority_factory     import *


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

