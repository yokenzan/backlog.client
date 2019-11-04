# -*- coding: utf-8 -*-

from typing import Union, Optional


class Config:

    def __init__(self, json: dict):
        self.json = json

    def get_project_id_or_key(self) -> Union[str, int, None]:
        return self.json.get('projectId') or self.json.get('projectKey')

    def get_api_key(self) -> Optional[str]:
        return self.json.get('apiKey')

    def get_workspace(self) -> Optional[str]:
        return self.json.get('workspace')
