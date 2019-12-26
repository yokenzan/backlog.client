# -*- coding: utf-8 -*-

import unittest
from unittest_data_provider import data_provider

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

    __provide_test_getters = lambda: [
        [1, 'kenshin', 'Himura Kenshin',  1, ],
        [2, 'zansa',   'Sagara Sanosuke', 2, ],
        [3, 'yahhy',   'Myojin Yahiko',   3, ],
        [4, 'himura',  'himura battosai', 3, ],
    ]

    @data_provider(__provide_test_getters)
    def test_getters(self, id: int, key_id: str, name: str, role_type: int):
        user = User(id, key_id, name, role_type)

        self.assertEqual(id,        user.id)
        self.assertEqual(key_id,    user.userId)
        self.assertEqual(name,      user.name)
        self.assertEqual(role_type, user.roleType)

