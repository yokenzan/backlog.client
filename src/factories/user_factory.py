# -*- coding: utf-8 -*-

from typing   import Optional
from src.user import *


class UserFactory:

    def generate(self, params: Optional[dict]) -> Optional[User]:
        if params is None:
            return None
        else:
            return User(params['id'], params['userId'], params['name'], params['roleType'])


