# -*- coding: utf-8 -*-


from typing        import List
from src.models    import Priority
from src.factories import PriorityFactory
from src.api       import AbstractClient

class getPriorities:

    def __init__(self, client: AbstractClient, factory: PriorityFactory):
        self.client  = client
        self.factory = factory

    def handle(self) -> List[Priority]:
        return [self.factory.generate(issue) for issue in self.client.get_priorities()]

