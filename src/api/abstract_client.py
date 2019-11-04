# -*- coding: utf-8 -*-

from typing import Union
from abc    import *

class AbstractClient(metaclass = ABCMeta):

    @abstractmethod
    def get_users(self) -> dict:
        raise NotImplementedError()

    @abstractmethod
    def get_statuses(self) -> dict:
        raise NotImplementedError()

    @abstractmethod
    def get_projects(self) -> dict:
        raise NotImplementedError()

    @abstractmethod
    def get_priorities(self) -> dict:
        raise NotImplementedError()

    @abstractmethod
    def get_categories(self) -> dict:
        raise NotImplementedError()

    @abstractmethod
    def get_issue_types(self) -> dict:
        raise NotImplementedError()

    @abstractmethod
    def get_project_users(self, project_id_or_key: Union[int, str]) -> dict:
        raise NotImplementedError()

