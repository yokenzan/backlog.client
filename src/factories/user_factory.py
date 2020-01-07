# -*- coding: utf-8 -*-

from typing import Optional

from src.models import User


class UserFactory:
    def generate(self, params: Optional[dict]) -> Optional[User]:
        if params is None:
            return None

        return User(
            params["id"],
            params["userId"],
            params["name"],
            params["roleType"]
        )
