# -*- coding: utf-8 -*-

import subprocess
from typing import List, Optional


class SubProcessRunner:
    '''
    Runs subeprocces and Returns STDOUT as string.
    '''
    def run(self, args: List[str]) -> Optional[str]:
        '''
        Runs sub procces.

        Parameters
        ----------
        args : List[str]
            A list of command and its arguments to execute.

        Returns
        -------
        str
            Returns STDOUT of run process.
        '''
        result = subprocess.run(
            args,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        return result.stdout.decode().strip()
