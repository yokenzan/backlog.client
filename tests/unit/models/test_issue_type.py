# -*- coding: utf-8 -*-

import unittest
from unittest_data_provider import data_provider

from src.models import IssueType


class IssueTypeTest(unittest.TestCase):
    def setUp(self):
        self.issue_type_id    = 1
        self.issue_type_name  = "ISSUE_TYPE_NAME"
        self.issue_type_color = "#FFFF00"
        self.issue_type_order = 1
        self.issue_type       = IssueType(
            self.issue_type_id,
            self.issue_type_name,
            self.issue_type_color,
            self.issue_type_order
        )

    def test_can_convert_into_list_item(self):
        """
        リストの文字列化できること
        """
        self.assertEqual(
            f"{str(self.issue_type_id)} # {str(self.issue_type_name)} {str(self.issue_type_color)}",
            self.issue_type.to_list_item()
        )

    def test_can_convert_into_string(self):
        """
        文字列化できること
        """
        self.assertEqual(str(self.issue_type_name), str(self.issue_type))

    __provide_test_getters = lambda: [
        [1, 'タスク', '#7ea800', 1, ],
        [2, 'バグ',   '#e30000', 2, ],
        [3, '要望',   '#ff9200', 3, ],
        [4, 'その他', '#2779ca', 4, ],
    ]

    @data_provider(__provide_test_getters)
    def test_getters(self, id: int, name: str, color: str, order: int):
        issue_type = IssueType(id, name, color, order)

        self.assertEqual(id,    issue_type.id)
        self.assertEqual(name,  issue_type.name)
        self.assertEqual(color, issue_type.color)
        self.assertEqual(order, issue_type.order)
