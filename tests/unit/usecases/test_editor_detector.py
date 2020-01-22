# -*- coding: utf-8 -*-


import os
import subprocess
import unittest

from src.config   import Config
from src.usecases import EditorDetector
from src.usecases import SubProcessRunner

class EditorDetectorTest(unittest.TestCase):
    def test_config_is_prior_to_others(self):
        config_editor = 'configured editor'
        config        = Config({ 'editor': config_editor })
        detector      = EditorDetector(config, SubProcessRunner())

        self.assertEqual(config_editor, detector.detect())

    def test_env_has_secondaly_highest_priority(self):
        os.environ['EDITOR'] = 'ENV EDITOR'

        self.assertEqual(
            os.getenv('EDITOR'),
            EditorDetector(Config({}), SubProcessRunner()).detect()
        )

    def test_vi_path_is_returnd_if_neigther_of_config_nor_env_exists(self):
        os.environ.pop('EDITOR')

        self.assertEqual(
            subprocess.check_output(['which', 'vi']).decode().strip(),
            EditorDetector(Config({}), SubProcessRunner()).detect()
        )
