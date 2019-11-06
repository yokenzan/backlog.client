# -*- coding: utf-8 -*-


from typing        import List
from src.models    import User
from src.factories import UserFactory
from src.api       import AbstractClient

class GetUsers:

    def __init__(self, client: AbstractClient, factory: UserFactory):
        self.client  = client
        self.factory = factory

    def handle(self) -> List[User]:
        return [self.factory.generate(issue) for issue in self.client.get_users()]

