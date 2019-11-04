# -*- coding: utf-8 -*-

from src.models import Priority

class PriorityFactory:

    def generate(self, params: dict) -> Priority:
        return Priority(params['id'], params['name'])

