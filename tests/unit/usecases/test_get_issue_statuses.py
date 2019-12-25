# -*- coding: utf-8 -*-


import unittest

from src.api import AbstractClient
from src.models import IssueStatus
from src.factories import IssueStatusFactory
from src.usecases import GetIssueStatuses

class GetIssueStatusesTest(unittest.TestCase):

    def test_returns_issue_statuses(self):
        list = self.make_usecase().handle()

        self.assertEqual(4, len(list))
        [self.assertIsInstance(issue_status, IssueStatus) for issue_status in list]

    def make_usecase(self) -> GetIssueStatuses:
        client_api = type("TestAbstractClientMock", (AbstractClient, ), {
            "get_issue_statuses": lambda: [
                {'id': 1, 'name': 'Open',        'color': '#ff0000', 'displayOrder': 1, },
                {'id': 2, 'name': 'In Progress', 'color': '#0000ff', 'displayOrder': 2, },
                {'id': 3, 'name': 'Resolved',    'color': '#00ff00', 'displayOrder': 3, },
                {'id': 4, 'name': 'Close',       'color': '#ccffa0', 'displayOrder': 4, },
            ],
        })
        factory    = IssueStatusFactory()

        return GetIssueStatuses(client_api, factory)
