# -*- coding: utf-8 -*-

import subprocess
import os


class LaunchEditor:

    def handle(self, edit_file: str):
        subprocess.run([self.__detect_editor(), edit_file])

    def __detect_editor(self) -> str:
        preferred_editor = os.environ.get('EDITOR')

        if preferred_editor is not None:
            return preferred_editor
        else:
            return subprocess.run(['which', 'vi'])

