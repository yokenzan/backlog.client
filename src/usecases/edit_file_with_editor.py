# -*- coding: utf-8 -*-

import os
import subprocess
from src.config import Config


class EditFileWithEditor:
    '''
    Command to edit file with editor.

    Attributes
    ----------
    config : Config
        Configuration values.
    '''

    def __init__(self, config: Config):
        self.config = config

    def handle(self, edit_file: str):
        '''
        Launch editor and edit file with it.

        Parameters
        ----------
        edit_file : str
            path of file to edit.
        '''
        subprocess.run([self.__detect_editor(), edit_file], check=True)

    def __detect_editor(self) -> str:
        '''
        Detect editor launcher command.

        Returns
        -------
        str
            Returns a command string treated as an editor launcher.
        '''
        preferred_editor = self.config.get_editor()

        if preferred_editor is not None:
            return preferred_editor

        preferred_editor = os.environ.get('EDITOR')

        if preferred_editor is not None:
            return preferred_editor

        return subprocess.run(['which', 'vi'], check=True)
