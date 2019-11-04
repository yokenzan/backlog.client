# -*- coding: utf-8 -*-

from typing           import Union
from BacklogPy        import Backlog
from .abstract_client import *
from src.config       import Config

class Client(AbstractClient):

    def __init__(self, config: Config):
        self.config = config
        self.client = Backlog(
            config.get_workspace(), config.get_api_key()
        )

    def get_users(self) -> dict:
        return self.get_project_users(
            self.config.get_project_id_or_key()
        )

    def get_issue_statuses(self) -> dict:
        return self.client.get_status_list().json()

    def get_projects(self) -> dict:
        return self.client.get_project_list().json()

    def get_priorities(self) -> dict:
        return self.client.get_priority_list().json()

    def get_categories(self) -> dict:
        return self.client.get_category_list(
            self.config.get_project_id_or_key()
        ).json()

    def get_issue_types(self) -> dict:
        return self.client.get_issue_type_list(
            self.config.get_project_id_or_key()
        ).json()

    def get_project_users(self, project_id_or_key: Union[int, str]) -> dict:
        return self.client.get_project_user_list(project_id_or_key).json()

