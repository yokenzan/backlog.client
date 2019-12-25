# -*- coding: utf-8 -*-


import unittest

from src.api import AbstractClient
from src.models import IssueType
from src.factories import IssueTypeFactory
from src.usecases import GetIssueTypes

class GetIssueTypesTest(unittest.TestCase):

    def test_returns_issue_types(self):
        list = self.make_usecase().handle()

        self.assertEqual(4, len(list))
        [self.assertIsInstance(issue_type, IssueType) for issue_type in list]

    def make_usecase(self) -> GetIssueTypes:
        client_api = type("TestAbstractClientMock", (AbstractClient, ), {
            "get_issue_types": lambda: [
                {'id': 1, 'name': 'タスク', 'color': '#7ea800', 'displayOrder': 1, },
                {'id': 2, 'name': 'バグ',   'color': '#e30000', 'displayOrder': 2, },
                {'id': 3, 'name': '要望',   'color': '#ff9200', 'displayOrder': 3, },
                {'id': 4, 'name': 'その他', 'color': '#2779ca', 'displayOrder': 4, },
            ],
        })
        factory    = IssueTypeFactory()

        return GetIssueTypes(client_api, factory)
