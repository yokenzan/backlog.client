# -*- coding: utf-8 -*-

import json
from typing import Union, Optional, TypeVar


T = TypeVar('T', bound = 'Config')


class Config:

    @classmethod
    def load(cls, config_path: str) -> T:
        with open(config_path) as f: return cls(json.load(f))

    def __init__(self, json: dict):
        self.json = json

    def get_project_id_or_key(self) -> Union[str, int, None]:
        return self.json.get('projectId') or self.json.get('projectKey')

    def get_api_key(self) -> Optional[str]:
        return self.json.get('apiKey')

    def get_workspace(self) -> Optional[str]:
        return self.json.get('workspace')
