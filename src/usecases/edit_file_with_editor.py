# -*- coding: utf-8 -*-

from .editor_detector    import EditorDetector
from .sub_process_runner import SubProcessRunner


class EditFileWithEditor:
    '''
    Command to edit file with editor.

    Attributes
    ----------
    editor_detector : EditorDetector
        Object resolving editor launcher command.
    sub_process_runner : SubProcessRunner
        Runs sub procces.
    '''

    def __init__(
            self,
            editor_detector:    EditorDetector,
            sub_process_runner: SubProcessRunner
    ):
        self.editor_detector    = editor_detector
        self.sub_process_runner = sub_process_runner

    def handle(self, edit_file: str):
        '''
        Launchs editor and edit file with it.

        Parameters
        ----------
        edit_file : str
            path of file to edit.
        '''
        self.sub_process_runner.run([
            self.editor_detector.detect(),
            edit_file
        ])
