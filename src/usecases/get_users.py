# -*- coding: utf-8 -*-


from typing import List

from src.api       import AbstractClient
from src.factories import UserFactory
from src.models    import User


class GetUsers:
    def __init__(self, client: AbstractClient, factory: UserFactory):
        self.client  = client
        self.factory = factory

    def handle(self) -> List[User]:
        """
        Executes fetching from API.
        """
        return [
            self.factory.generate(issue) for issue in self.client.get_users()
        ]
