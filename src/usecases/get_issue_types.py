# -*- coding: utf-8 -*-


from typing import List

from src.api       import AbstractClient
from src.factories import IssueTypeFactory
from src.models    import IssueType


class GetIssueTypes:
    '''
    Gets issue types by API client.
    '''

    def __init__(self, client: AbstractClient, factory: IssueTypeFactory):
        self.client  = client
        self.factory = factory

    def handle(self) -> List[IssueType]:
        '''
        Executes fetching from API.
        '''
        return [
            self.factory.generate(issue)
            for issue in self.client.get_issue_types()
        ]
