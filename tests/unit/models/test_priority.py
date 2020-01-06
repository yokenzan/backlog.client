# -*- coding: utf-8 -*-


import unittest

from src.models.priority import Priority


class PriorityTest(unittest.TestCase):
    def setUp(self):
        self.priority_id   = 1
        self.priority_name = "VERY HIGH"
        self.priority      = Priority(self.priority_id, self.priority_name)

    def test_can_convert_into_list_item(self):
        self.assertEqual(
            f"{str(self.priority_id)} # {str(self.priority_name)}",
            self.priority.to_list_item()
        )

    def test_can_convert_into_string(self):
        self.assertEqual(
            f"{str(self.priority_id)}, {str(self.priority_name)}",
            str(self.priority)
        )
