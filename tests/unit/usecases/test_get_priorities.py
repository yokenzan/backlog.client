# -*- coding: utf-8 -*-


import unittest

from src.api import AbstractClient
from src.models import Priority
from src.factories import PriorityFactory
from src.usecases import GetPriorities

class GetPrioritiesTest(unittest.TestCase):

    def test_returns_priorities(self):
        list = self.make_usecase().handle()

        self.assertEqual(3, len(list))
        [self.assertIsInstance(priority, Priority) for priority in list]

    def make_usecase(self) -> GetPriorities:
        client_api = type("TestAbstractClientMock", (AbstractClient, ), {
            "get_priorities": lambda: [
                {'id': 1, 'name': 'High',   },
                {'id': 2, 'name': 'Normal', },
                {'id': 3, 'name': 'Low',    },
            ],
        })
        factory    = PriorityFactory()

        return GetPriorities(client_api, factory)
