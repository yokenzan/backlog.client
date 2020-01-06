# -*- coding: utf-8 -*-

import json
from typing import Optional, TypeVar, Union


TypeSelf = TypeVar('TypeSelf', bound='Config')


class Config:
    '''
    Configuration class wrapping a dictionary.

    Attributes
    ----------
    json : dict
        a dictionary of configuration values
    '''

    @classmethod
    def load(cls, config_path: str) -> TypeSelf:
        '''
        Load configurations from config file and create new instance with it.

        Parameters
        ----------
        config_path : str
            path of config file.

        Returns
        -------
        TypeSelf
            Returns new instance with loaded configuration values.
        '''

        with open(config_path) as config_file:
            return cls(json.load(config_file))

    def __init__(self, json_dict: dict):
        self.json = json_dict

    def get_project_id_or_key(self) -> Union[str, int, None]:
        '''
        Gets project id or key.
        '''

        return self.json.get('projectId') or self.json.get('projectKey')

    def get_api_key(self) -> Optional[str]:
        '''
        Gets API key.
        '''

        return self.json.get('apiKey')

    def get_workspace(self) -> Optional[str]:
        '''
        Gets workspace key.
        '''

        return self.json.get('workspace')

    def get_editor(self) -> Optional[str]:
        '''
        Gets editor launcher command.
        '''

        return self.json.get('editor')
