# -*- coding: utf-8 -*-

import unittest

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
