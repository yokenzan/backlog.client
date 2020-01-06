# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod
from typing import Union


class AbstractClient(metaclass=ABCMeta):
    '''
    Abstract API client class to connect with Backlog web API.
    '''

    @abstractmethod
    def get_users(self) -> dict:
        '''
        Gets user list from web API as a dictionay.

        Returns
        -------
        dict

        Raises
        ------
        NotImplementedError
            Raises when this method is not overriden by sub class.
        '''
        raise NotImplementedError()

    @abstractmethod
    def get_projects(self) -> dict:
        '''
        Gets assigned project list of current user from API as a dictionary.

        Returns
        -------
        dict

        Raises
        ------
        NotImplementedError
            Raises when this method is not overriden by sub class.
        '''
        raise NotImplementedError()

    @abstractmethod
    def get_priorities(self) -> dict:
        '''
        Gets issue priority list of current project from API as a dictionary.

        Returns
        -------
        dict

        Raises
        ------
        NotImplementedError
            Raises when this method is not overriden by sub class.
        '''
        raise NotImplementedError()

    @abstractmethod
    def get_categories(self) -> dict:
        '''
        Gets project users of current project list from API as a dictionary.

        Returns
        -------
        dict

        Raises
        ------
        NotImplementedError
            Raises when this method is not overriden by sub class.
        '''
        raise NotImplementedError()

    @abstractmethod
    def get_issue_types(self) -> dict:
        '''
        Gets issue type list of current project from API as a dictionary.

        Returns
        -------
        dict

        Raises
        ------
        NotImplementedError
            Raises when this method is not overriden by sub class.
        '''
        raise NotImplementedError()

    @abstractmethod
    def get_issue_statuses(self) -> dict:
        '''
        Gets project issue status list from API as a dictionary.

        Returns
        -------
        dict

        Raises
        ------
        NotImplementedError
            Raises when this method is not overriden by sub class.
        '''
        raise NotImplementedError()

    @abstractmethod
    def get_project_users(self, project_id_or_key: Union[int, str]) -> dict:
        '''
        Gets project user list from API as a dictionary.

        Returns
        -------
        dict

        Raises
        ------
        NotImplementedError
            Raises when this method is not overriden by sub class.
        '''
        raise NotImplementedError()

