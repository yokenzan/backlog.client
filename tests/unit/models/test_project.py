# -*- coding: utf-8 -*-


import unittest
from unittest_data_provider import data_provider

from src.models.project import Project

class ProjectTest(unittest.TestCase):

    def test_can_convert_into_string(self):
        params  = [1, 'PR', 'テストプロジェクト']
        project = Project(*params)

        self.assertEqual(
            'Project: ' + ', '.join([str(x) for x in params]),
            str(project)
        )

    __provide_test_getters = lambda: [
        [1, 'PR', 'PROJECT_PR'],
        [2, 'JC', 'PROJECT_JC'],
        [3, 'PP', 'PROJECT_PP'],
    ]

    @data_provider(__provide_test_getters)
    def test_getters(self, id: int, key: str, name: str):
        project = Project(id, key, name)

        self.assertEqual(id,   project.id)
        self.assertEqual(key,  project.key)
        self.assertEqual(name, project.name)

