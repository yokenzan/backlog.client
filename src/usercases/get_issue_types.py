# -*- coding: utf-8 -*-


from typing        import List
from src.models    import IssueType
from src.factories import IssueTypeFactory
from src.api       import AbstractClient

class GetIssueTypes:

    def __init__(self, client: AbstractClient, factory: IssueTypeFactory):
        self.client  = client
        self.factory = factory

    def handle(self) -> List[IssueType]:
        return [self.factory.generate(issue) for issue in self.client.get_issue_types()]
