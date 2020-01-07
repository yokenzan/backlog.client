# -*- coding: utf-8 -*-

import os
from src.config import Config

from .sub_process_runner import SubProcessRunner


class EditorDetector:
    '''
    Detects editor launcher command.

    Attributes
    ----------
    config : Config
        Configuration values.
    sub_process_runner : SubProcessRunner
        An object running sub procces.
    '''

    def __init__(
            self,
            config: Config,
            sub_process_runner: SubProcessRunner
    ):
        self.config = config
        self.sub_process_runner = sub_process_runner

    def detect(self) -> str:
        '''
        Detects editor launcher command.

        Returns
        -------
        str
            Returns a command string treated as an editor launcher.
        '''
        preferred_editor = self.config.get_editor()

        if preferred_editor is not None:
            return preferred_editor

        return os.getenv(
            'EDITOR',
            self.sub_process_runner.run(['which', 'vi'])
        )
