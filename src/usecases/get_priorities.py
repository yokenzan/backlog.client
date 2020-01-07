# -*- coding: utf-8 -*-


from typing import List

from src.api import AbstractClient
from src.factories import PriorityFactory
from src.models import Priority


class GetPriorities:
    """
    Gets issue priorities by API client.
    """

    def __init__(self, client: AbstractClient, factory: PriorityFactory):
        self.client = client
        self.factory = factory

    def handle(self) -> List[Priority]:
        """
        Executes fetching from API.
        """
        return [
            self.factory.generate(issue)
            for issue in self.client.get_priorities()
        ]
