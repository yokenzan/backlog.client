# -*- coding: utf-8 -*-

import unittest

from src.models import IssueStatus


class IssueStatusTest(unittest.TestCase):
    def setUp(self):
        self.issue_status_id    = 1
        self.issue_status_name  = "issue_status_NAME"
        self.issue_status_color = "#FFFF00"
        self.issue_status_order = 1
        self.issue_status       = IssueStatus(
            self.issue_status_id,
            self.issue_status_name,
            self.issue_status_color,
            self.issue_status_order
        )

    def test_can_convert_into_list_item(self):
        """
        リストの文字列化できること
        """
        self.assertEqual(
            f"{str(self.issue_status_id)} # {str(self.issue_status_name)} {str(self.issue_status_color)}",
            self.issue_status.to_list_item()
        )

    def test_can_convert_into_string(self):
        """
        文字列化できること
        """
        self.assertEqual(str(self.issue_status_name), str(self.issue_status))
