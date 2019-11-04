# -*- coding: utf-8 -*-


from typing        import List
from src.models    import IssueStatus
from src.factories import IssueStatusFactory
from src.api       import AbstractClient

class GetIssueStatuses:

    def __init__(self, client: AbstractClient, factory: IssueStatusFactory):
        self.client  = client
        self.factory = factory

    def handle(self) -> List[IssueStatus]:
        return [self.factory.generate(issue) for issue in self.client.get_issue_statuses()]

