# -*- coding: utf-8 -*-

import unittest

from src.models import User


class UserTest(unittest.TestCase):
    def setUp(self):
        self.user_id     = 1
        self.user_key_id = "USER_KEY"
        self.user_name   = "USER_NAME"
        self.role_type   = 1
        self.user        = User(
            self.user_id, self.user_key_id, self.user_name, self.role_type
        )

    def test_can_convert_into_list_item(self):
        """
        リストの文字列化できること
        """
        self.assertEqual(
            f"{str(self.user_id)} # {str(self.user_name)}",
            self.user.to_list_item()
        )

    def test_can_convert_into_string(self):
        """
        文字列化できること
        """
        self.assertEqual(str(self.user_name), str(self.user))
