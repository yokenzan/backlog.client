# -*- coding: utf-8 -*-


import subprocess
import unittest

from src.usecases import SubProcessRunner

class SubProcessRunnerTest(unittest.TestCase):

    def test_runs_subprocess(self):
        args = ['which', 'vi']

        self.assertEqual(
            subprocess.getoutput(' '.join(args)),
            SubProcessRunner().run(args)
        )

    def test_raises_exception_when_process_failed_by_executing_unknown_command(self):
        with self.assertRaises(FileNotFoundError):
            SubProcessRunner().run(['UNKNOWN_COMMAND'])

    def test_raises_exception_when_process_failed_while_executing_command(self):
        with self.assertRaises(subprocess.CalledProcessError):
            SubProcessRunner().run(['mkdir', '.'])
