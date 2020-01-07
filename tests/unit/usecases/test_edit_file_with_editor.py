# -*- coding: utf-8 -*-


import unittest
from unittest.mock import Mock

from src.usecases import EditFileWithEditor
from src.usecases import EditorDetector
from src.usecases import SubProcessRunner

class EditFileWithEditorTest(unittest.TestCase):
    def test_edit_specified_file_with_detected_editor(self):
        # preparation

        editor = 'detected editor command'

        detector = Mock(spec=EditorDetector)
        detector.detect.return_value = editor

        runner = Mock(spec=SubProcessRunner)

        filename = 'edit filename'

        # execution

        EditFileWithEditor(detector, runner).handle(filename)

        # assertion

        runner.run.assert_called_once_with([editor, filename])
