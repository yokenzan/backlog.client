# -*- coding: utf-8 -*-


import unittest
from src.models.project import Project

class ProjectTest(unittest.TestCase):

    def test_can_convert_into_string(self):
        """
        文字列化できること
        """
        params  = [1, 'PR', 'テストプロジェクト']
        project = Project(*params)

        self.assertEqual(
            'Project: ' + ', '.join([str(x) for x in params]),
            str(project)
        )
